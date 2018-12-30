from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string
from cardiacpedia import db
from cardiacpedia.models import user_manager
from cardiacpedia.models import IPG
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

devices = Blueprint('devices', __name__)

################################################################################
##############################View Table########################################
################################################################################
@devices.route('/devices/ipg')
@login_required
def ipg():
    page = request.args.get('page', 1, type=int)
    devices = IPG.query.paginate(page=page, per_page=10)
    return render_template('ipg.html', devices=devices, page_title='IPG Low-Voltage Devices')
