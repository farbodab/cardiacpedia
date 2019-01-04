from flask import render_template, url_for, flash, redirect, request, Blueprint
from cardiacpedia import db
from cardiacpedia.models import *
from cardiacpedia.devices.forms import *
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


devices = Blueprint('devices', __name__)

@devices.route('/devices/compatibility', methods=['GET', 'POST'])
@login_required
def compatibility():
    form = Devices()
    if form.validate_on_submit():
        if form.type.data == 'IPG':
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data, nbg=form.paced.data + form.sensed.data))
        elif form.type.data == 'CRTP':
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data, nbg=form.paced.data + form.sensed.data))
        elif form.type.data == 'ICD':
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data, nbg=form.paced.data + form.sensed.data))
        elif form.type.data == 'CRTD':
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data, nbg=form.paced.data + form.sensed.data))
        elif form.type.data == 'LV':
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data, nbg=form.paced.data + form.sensed.data))
        elif form.type.data == 'HV':
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data, nbg=form.paced.data + form.sensed.data))
    return render_template('/Devices/compatible_finder.html', page_title="Compatible Device Finder", form=form)


@devices.route('/devices/finder', methods=['GET', 'POST'])
@login_required
def finder():
    form = Finder()
    if form.validate_on_submit():
        if form.type.data == 'IPG':
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))
        elif form.type.data == 'CRTP':
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))
        elif form.type.data == 'ICD':
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))
        elif form.type.data == 'CRTD':
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))
        elif form.type.data == 'LV':
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))
        elif form.type.data == 'HV':
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    return render_template('/Devices/finder.html', page_title="Device Finder", form=form)


################################################################################
##############################View Table########################################
################################################################################
@devices.route('/devices/ipg', methods=['GET', 'POST'])
@login_required
def ipg():
    form = Find_Device()
    if form.validate_on_submit():
        return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    nbg = request.args.get('nbg')
    devices = IPG.query
    if manufacturer:
        devices = devices.filter(IPG.manufacturer.like('%' + manufacturer + '%'))
        form.manufacturer.data = manufacturer
    if model_number:
        devices = devices.filter(IPG.model_number.like('%' + model_number + '%' ))
        form.model_number.data = model_number
    if device_name:
        devices = devices.filter(IPG.name.like('%' + device_name + '%' ))
        form.name.data = device_name
    if nbg:
        devices = devices.filter(IPG.nbg_code.like(nbg[0] + nbg[1] + '%'))
    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='IPG Low-Voltage Devices', form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, nbg=nbg)

@devices.route('/devices/ipg/<id>')
@login_required
def ipg_device(id):
    devices = IPG.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/ipg_device.html', device=devices, page_title=devices.model_number)


@devices.route('/devices/crtp', methods=['GET', 'POST'])
@login_required
def crtp():
    form = Find_Device()
    if form.validate_on_submit():
        return redirect(url_for('devices.crtp',page_title='CRT-P Low-Voltage Devices', manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    devices = CRTP.query
    if manufacturer:
        devices = devices.filter(CRTP.manufacturer.like('%' + manufacturer + '%'))
        form.manufacturer.data = manufacturer
    if model_number:
        devices = devices.filter(CRTP.model_number.like('%' + model_number + '%' ))
        form.model_number.data = model_number
    if device_name:
        devices = devices.filter(CRTP.name.like('%' + device_name + '%' ))
        form.name.data = device_name
    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='CRT-P Low-Voltage Devices', form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name)



@devices.route('/devices/crtp/<id>')
@login_required
def crtp_device(id):
    devices = CRTP.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/crtp_device.html', device=devices, page_title=devices.model_number)

@devices.route('/devices/crtd', methods=['GET', 'POST'])
@login_required
def crtd():
    form = Find_Device()
    if form.validate_on_submit():
        return redirect(url_for('devices.crtd',page_title='CRT-D High Voltage Devices', manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    devices = CRTD.query
    if manufacturer:
        devices = devices.filter(CRTD.manufacturer.like('%' + manufacturer + '%'))
        form.manufacturer.data = manufacturer
    if model_number:
        devices = devices.filter(CRTD.model_number.like('%' + model_number + '%' ))
        form.model_number.data = model_number
    if device_name:
        devices = devices.filter(CRTD.name.like('%' + device_name + '%' ))
        form.name.data = device_name
    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='CRT-D High Voltage Devices',
    form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name)



@devices.route('/devices/crtd/<id>')
@login_required
def crtd_device(id):
    devices = CRTD.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/crtd_device.html', device=devices, page_title=devices.model_number)

@devices.route('/devices/hv', methods=['GET', 'POST'])
@login_required
def hv():
    form = Find_Device()
    if form.validate_on_submit():
        return redirect(url_for('devices.hv',page_title='HV High-Voltage Leads', manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    devices = HV.query
    if manufacturer:
        devices = devices.filter(HV.manufacturer.like('%' + manufacturer + '%'))
        form.manufacturer.data = manufacturer
    if model_number:
        devices = devices.filter(HV.model_number.like('%' + model_number + '%' ))
        form.model_number.data = model_number
    if device_name:
        devices = devices.filter(HV.name.like('%' + device_name + '%' ))
        form.name.data = device_name
    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='HV High-Voltage Leads', form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name)



@devices.route('/devices/hv/<id>')
@login_required
def hv_device(id):
    devices = HV.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/hv_device.html', device=devices, page_title=devices.model_number)


@devices.route('/devices/icd', methods=['GET', 'POST'])
@login_required
def icd():
    form = Find_Device()
    if form.validate_on_submit():
        return redirect(url_for('devices.icd',page_title='ICD High-Voltage Devices', manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    devices = ICD.query
    if manufacturer:
        devices = devices.filter(ICD.manufacturer.like('%' + manufacturer + '%'))
    if model_number:
        devices = devices.filter(ICD.model_number.like('%' + model_number + '%' ))
    if device_name:
        devices = devices.filter(ICD.name.like('%' + device_name + '%' ))
    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='ICD High-Voltage Devices', form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name)



@devices.route('/devices/icd/<id>')
@login_required
def icd_device(id):
    devices = ICD.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/icd_device.html', device=devices, page_title=devices.model_number)

@devices.route('/devices/lv', methods=['GET', 'POST'])
@login_required
def lv():
    form = Find_Device()
    if form.validate_on_submit():
        return redirect(url_for('devices.lv',page_title='LV Low-Voltage Devices', manufacturer=form.manufacturer.data, model_number=form.model_number.data, device_name=form.name.data))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    devices = LV.query
    if manufacturer:
        devices = devices.filter(LV.manufacturer.like('%' + manufacturer + '%'))
        form.manufacturer.data = manufacturer
    if model_number:
        devices = devices.filter(LV.model_number.like('%' + model_number + '%' ))
        form.model_number.data = model_number
    if device_name:
        devices = devices.filter(LV.name.like('%' + device_name + '%' ))
        form.name.data = device_name
    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='LV Low-Voltage Devices', form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name)



@devices.route('/devices/lv/<id>')
@login_required
def lv_device(id):
    devices = LV.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/lv_device.html', device=devices, page_title=devices.model_number)
