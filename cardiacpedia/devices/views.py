from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string
from cardiacpedia import db
from cardiacpedia.models import user_manager,IPG
from cardiacpedia.devices.forms import Find_IPG
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


devices = Blueprint('devices', __name__)

################################################################################
##############################View Table########################################
################################################################################
@devices.route('/devices/ipg', methods=['GET', 'POST'])
@login_required
def ipg():
    form = Find_IPG()
    if form.validate_on_submit():
        page = request.args.get('page', 1, type=int)
        devices = IPG.query
        FILTERS = [form.manufacturer.data, form.model_number.data, form.name.data]
        NAMES = [IPG.manufacturer, IPG.model_number, IPG.name]
        if form.manufacturer.data:
            devices = devices.filter(IPG.manufacturer.like('%' + form.manufacturer.data + '%'))
        if form.model_number.data:
            devices = devices.filter(IPG.model_number.like('%' + form.model_number.data + '%' ))
        if form.name.data:
            devices = devices.filter(IPG.name.like('%' + form.name.data + '%' ))
        devices = devices.paginate(page=page, per_page=10)
        return render_template('ipg.html', devices=devices, page_title='IPG Low-Voltage Devices', form=form)

    page = request.args.get('page', 1, type=int)
    devices = IPG.query.paginate(page=page, per_page=10)
    return render_template('ipg.html', devices=devices, page_title='IPG Low-Voltage Devices', form=form)
