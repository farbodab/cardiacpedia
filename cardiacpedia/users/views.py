from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string, session
from cardiacpedia import db, requires_access_level
from werkzeug.security import generate_password_hash,check_password_hash
from cardiacpedia.models import *
from cardiacpedia.users.forms import *
from cardiacpedia.core.forms import *
from flask_login import login_user, current_user, logout_user, login_required
import stripe
import json
import datetime

stripe_keys = {
  'secret_key': 'sk_test_sUBjEZ7otbSikPzwk3HPVZb0',
  'publishable_key': 'pk_test_dtOoNU1AqHUdKNcjSaL7iZ7m'
}

stripe.api_key = stripe_keys['secret_key']


users = Blueprint('users', __name__)

@users.route('/youraccount')
@login_required
def account():
    if current_user.customer_id:
        customer = stripe.Customer.retrieve(current_user.customer_id)
        customer_json = str(customer)
        customer_params = json.loads(customer_json)
        last4 = customer_params['sources']['data'][0]["last4"]
        brand = customer_params['sources']['data'][0]["brand"]
        subscription = stripe.Subscription.retrieve(current_user.plan_id)
        subscription_json = str(subscription)
        subscription_params = json.loads(subscription_json)
        amount = subscription_params['items']['data'][0]["plan"]["amount"]
        return render_template('account.html', page_title="CardiacBook", last4=last4, brand=brand, amount=amount, key=stripe_keys['publishable_key'])
    else:
        return render_template('account.html', page_title="CardiacBook")


@users.route('/changepayement', methods=['POST'])
@login_required
def change_payement():
    token = request.form['stripeToken']
    stripe.Customer.modify(current_user.customer_id,
     source=token,
    )
    flash('Payment updated')
    return redirect(url_for('users.account'))

@users.route('/register', methods=['GET','POST'])
def register():
    return render_template('step1.html', page_title="CardiacBook")

@users.route('/plans', methods=['GET','POST'])
def plans():
    if request.method == 'GET':
        return redirect(url_for('users.register'))
    form = Plan()
    return render_template('plan.html', page_title="CardiacBook", form=form)

@users.route('/setup', methods=['POST'])
def setup():
    form = Plan()
    if form.validate_on_submit():
        if form.monthly.data:
            session['Plan'] = 'First Timer'
        elif form.three.data:
            session['Plan'] = 'Pro'
        else:
            session['Plan'] = 'Platinum'
        return render_template('step2.html', page_title="CardiacBook")
    else:
        return redirect(url_for('users.register'))

@users.route('/cancelplan', methods=['GET','POST'])
@login_required
def cancel_plan():
    subscription = stripe.Subscription.retrieve(current_user.plan_id)
    subscription.delete()
    current_user.access = '1'
    current_user.plan = 'Free'
    current_user.customer_id = ''
    current_user.plan_id = ''
    db.session.commit()
    flash('We are sad to see you go. Your subscription has been cancelled effective immediately')
    return redirect(url_for('core.index'))

@users.route('/changeplan', methods=['GET','POST'])
@login_required
def change_plan():
    form = Plan()
    if form.validate_on_submit():
        if form.monthly.data:
            current_user.plan = 'First Timer'
        elif form.three.data:
            current_user.plan = 'Pro'
        else:
            current_user.plan = 'Platinum'
        db.session.commit()
        if current_user.plan_id:
            if form.monthly.data:
                subscription = stripe.Subscription.retrieve(current_user.plan_id)
                stripe.Subscription.modify(current_user.plan_id,
                  cancel_at_period_end=False,
                  items=[{
                    'id': subscription['items']['data'][0].id,
                    'plan': 'plan_EIZlCcrHyKftHU',
                  }]
                  )
                current_user.plan = 'First Timer'
            elif form.three.data:
                subscription = stripe.Subscription.retrieve(current_user.plan_id)
                stripe.Subscription.modify(current_user.plan_id,
                  cancel_at_period_end=False,
                  items=[{
                    'id': subscription['items']['data'][0].id,
                    'plan': 'plan_EIZlzeL9IipfX9',
                  }]
                  )
                current_user.plan = 'Pro'
            else:
                subscription = stripe.Subscription.retrieve(current_user.plan_id)
                stripe.Subscription.modify(current_user.plan_id,
                  cancel_at_period_end=False,
                  items=[{
                    'id': subscription['items']['data'][0].id,
                    'plan': 'plan_EIbSjTIV9tP1Q1',
                  }]
                  )
                current_user.plan = 'Platnium'
            db.session.commit()
            flash('Your plan has been updated')
            return redirect(url_for('users.account'))
        else:
            return redirect(url_for('users.pay'))
    return render_template('plan_special.html', page_title="CardiacBook", form=form)


@users.route('/email', methods=['GET','POST'])
@login_required
def email():
    form = EmailForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))
    return render_template('email.html', page_title="CardiacBook", form=form)

@users.route('/password', methods=['GET', 'POST'])
@login_required
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        current_user.password_hash = generate_password_hash(form.new_password.data)
        db.session.commit()
        flash('Password Updated')
        return redirect(url_for('users.account'))
    return render_template('password.html', page_title="CardiacBook", form=form)


@users.route('/account', methods=['GET', 'POST'])
def new_account():
    form = RegistrationForm()
    if form.validate_on_submit():
        plan = session['Plan']
        user = User(email=form.email.data,
                    password=form.password.data, plan=plan)

        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('users.pay'))
    return render_template('/Users/register.html', form=form)

@users.route('/pay')
@login_required
def pay():
    if current_user.allowed(2):
        return redirect(url_for('devices.home'))
    else:
        now = datetime.datetime.now()
        week_now = now + datetime.timedelta(days=7)
        plan = current_user.plan
        if plan == 'Pro':
            amount = 2499
        elif plan == 'Platinum':
            amount = 9999
        else:
            amount = 999
        return render_template('Users/pay.html', key=stripe_keys['publishable_key'], plan=plan, amount=amount, trial=week_now.strftime("%Y-%m-%d"))

@users.route('/charge', methods=['POST'])
@login_required
def charge():
    # Amount in cents
    plan = current_user.plan


    customer = stripe.Customer.create(
        email=current_user.email,
        source=request.form['stripeToken']
    )

    if plan == 'Pro':
        subscription = stripe.Subscription.create(
          customer=customer.id,
          items=[{'plan': 'plan_EIZlzeL9IipfX9',}],
          trial_period_days=7
        )
    elif plan == 'Platinum':
        subscription = stripe.Subscription.create(
          customer=customer.id,
          items=[{'plan': 'plan_EIbSjTIV9tP1Q1',}],
          trial_period_days=7
        )
    else:
        subscription = stripe.Subscription.create(
          customer=customer.id,
          items=[{'plan': 'plan_EIZlCcrHyKftHU',}],
          trial_period_days=7
        )

    current_user.customer_id = customer.id
    current_user.access = 2
    current_user.plan_id = subscription.id
    db.session.commit()
    flash('Welcome to CardiacBook!')
    return redirect(url_for('devices.home'))


@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user is not None and user.check_password(form.password.data):
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
    return render_template('/Users/login.html', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))

################################################################################
##############################View Users########################################
################################################################################
@users.route('/admin/users/view_users')
@requires_access_level(ACCESS['admin'])
def admin_users_view_users():
    if current_user:
        """
        Allows the admin to view all users in the system
        """
        users = User.query.order_by(User.id, User.email).all()
        return render_template('/Admin/view_users.html', users=users, page_title='View Users')
    else:
        flash('You do not have permission to access this page!')

################################################################################
##############################Remove Users########################################
################################################################################
@users.route('/admin/users/remove_users', methods=['GET', 'POST'])
@requires_access_level(ACCESS['admin'])
def admin_users_remove_users():

    form = Remove_Users()

    if form.validate_on_submit():
        User.query.filter_by(id=form.user_id.data).delete()
        db.session.commit()
        flash('User has been removed from the database.')
        return redirect(url_for('users.admin_users_view_users'))

    return render_template('/Admin/remove_users.html', form=form, page_title='Remove Users')


################################################################################
##############################Add User Roles#####################################
################################################################################

@users.route('/admin/users/add_user_roles', methods=['GET', 'POST'])
@requires_access_level(ACCESS['admin'])
def admin_users_add_user_roles():

    form = Add_User_Roles()

    if form.validate_on_submit():
        user = User.query.get(form.user_id.data)
        user.access = form.role_id.data
        db.session.commit()
        flash('Roles have been changed for this user.')
        return redirect(url_for('users.admin_users_view_users'))

    return render_template('/Admin/add_user_roles.html', form=form, page_title='Add User Roles')
