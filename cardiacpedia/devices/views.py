from flask import render_template, url_for, flash, redirect, request, Blueprint
from cardiacpedia import db
from cardiacpedia.models import *
from cardiacpedia.devices.forms import *
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


devices = Blueprint('devices', __name__)

@devices.route('/devices/new', methods=['GET', 'POST'])
@login_required
def new():
    form_type = Device_Type()
    form = Device_New()
    if form.validate_on_submit():
        if form_type.type.data == 'IPG':
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type='1'))
        elif form_type.type.data == 'CRTP':
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type='1'))
        elif form_type.type.data == 'ICD':
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type='1'))
        elif form_type.type.data == 'CRTD':
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type='1'))
    return render_template('/Devices/New/new_finder.html', page_title="New Device Finder", form_type=form_type, form=form)

@devices.route('/devices/compatibility', methods=['GET', 'POST'])
@login_required
def compatibility():
    form = Devices_Change()
    form_type = Device_Type()
    if form.validate_on_submit():
        if form_type.type.data == 'IPG':
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type='2'))
        elif form_type.type.data == 'CRTP':
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data,ra=form.ra.data, rv=form.rv.data, f_type='2'))
        elif form_type.type.data == 'ICD':
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data,ra=form.ra.data, rv=form.rv.data, f_type='2'))
        elif form_type.type.data == 'CRTD':
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data,ra=form.ra.data, rv=form.rv.data, f_type='2'))
        elif form_type.type.data == 'LV':
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data,ra=form.ra.data, rv=form.rv.data, f_type='2'))
        elif form_type.type.data == 'HV':
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data,ra=form.ra.data, rv=form.rv.data, f_type='2'))

    return render_template('/Devices/Change/compatible.html', page_title="Upgrade / PAC Change", form=form, form_type=form_type)


@devices.route('/devices/finder', methods=['GET', 'POST'])
@login_required
def finder():
    form = Device_Find()
    form_type = Device_Type()
    if form.validate_on_submit():
        if form_type.type.data == 'IPG':
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type='3'))
        elif form_type.type.data == 'CRTP':
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type='3'))
        elif form_type.type.data == 'ICD':
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type='3'))
        elif form_type.type.data == 'CRTD':
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type='3'))
        elif form_type.type.data == 'LV':
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type='3'))
        elif form_type.type.data == 'HV':
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type='3'))
    type = request.args.get('type')
    if type:
        form_type.type.data = type
    return render_template('/Devices/Finder/finder.html', page_title="Search All Devices", form=form, form_type=form_type)

@devices.route('/devices/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('/Devices/Home.html', page_title="Home")


################################################################################
##############################View Table########################################
################################################################################
@devices.route('/devices/ipg', methods=['GET', 'POST'])
@login_required
def ipg():
    f_type = request.args.get('f_type')
    if f_type == '1':
        form = Device_New()
        if form.validate_on_submit():
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type =f_type))
    elif f_type == '2':
        form = Devices_Change()
        if form.validate_on_submit():
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type =f_type))
    elif f_type == '3':
        form = Device_Find()
        if form.validate_on_submit():
            return redirect(url_for('devices.ipg',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type = f_type))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    paced = request.args.get('paced')
    sensed = request.args.get('sensed')
    ra = request.args.get('ra')
    rv = request.args.get('rv')

    nbg = ''

    if paced and sensed:
        nbg = paced + sensed
        form.paced.data = paced
        form.sensed.data = sensed
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
        devices = devices.filter(IPG.nbg_code.like(nbg + '%'))

    if ra:
        devices = devices.filter(IPG.ra.like(ra + '%'))
        form.ra.data = ra
    if rv:
        devices = devices.filter(IPG.rv.like(rv + '%'))
        form.rv.data = rv

    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='IPG Low-Voltage Devices',form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, sensed=sensed, paced=paced, f_type=f_type, ra=ra, rv=rv)

@devices.route('/devices/ipg/<id>')
@login_required
def ipg_device(id):
    devices = IPG.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/ipg_device.html', device=devices, page_title=devices.model_number)


@devices.route('/devices/crtp', methods=['GET', 'POST'])
@login_required
def crtp():
    f_type = request.args.get('f_type')
    if f_type == '1':
        form = Device_New()
        if form.validate_on_submit():
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type =f_type))
    elif f_type == '2':
        form = Devices_Change()
        if form.validate_on_submit():
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type =f_type))
    elif f_type == '3':
        form = Device_Find()
        if form.validate_on_submit():
            return redirect(url_for('devices.crtp',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type = f_type))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    paced = request.args.get('paced')
    sensed = request.args.get('sensed')
    ra = request.args.get('ra')
    rv = request.args.get('rv')

    nbg = ''

    if paced and sensed:
        nbg = paced + sensed
        form.paced.data = paced
        form.sensed.data = sensed
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
    if nbg:
        devices = devices.filter(CRTP.nbg_code.like(nbg + '%'))

    if ra:
        devices = devices.filter(CRTP.ra.like(ra + '%'))
        form.ra.data = ra
    if rv:
        devices = devices.filter(CRTP.rv.like(rv + '%'))
        form.rv.data = rv

    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='CRT-P Low-Voltage Devices',form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, sensed=sensed, paced=paced, f_type=f_type, ra=ra, rv=rv)


@devices.route('/devices/crtp/<id>')
@login_required
def crtp_device(id):
    devices = CRTP.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/crtp_device.html', device=devices, page_title=devices.model_number)

@devices.route('/devices/crtd', methods=['GET', 'POST'])
@login_required
def crtd():
    f_type = request.args.get('f_type')
    if f_type == '1':
        form = Device_New()
        if form.validate_on_submit():
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type =f_type))
    elif f_type == '2':
        form = Devices_Change()
        if form.validate_on_submit():
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type =f_type))
    elif f_type == '3':
        form = Device_Find()
        if form.validate_on_submit():
            return redirect(url_for('devices.crtd',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type = f_type))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    paced = request.args.get('paced')
    sensed = request.args.get('sensed')
    ra = request.args.get('ra')
    rv = request.args.get('rv')

    nbg = ''

    if paced and sensed:
        nbg = paced + sensed
        form.paced.data = paced
        form.sensed.data = sensed
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
    if nbg:
        devices = devices.filter(CRTD.nbg_code.like(nbg + '%'))
    if ra:
        devices = devices.filter(CRTD.ra.like(ra + '%'))
        form.ra.data = ra
    if rv:
        devices = devices.filter(CRTD.rv.like(rv + '%'))
        form.rv.data = rv

    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='CRT-D High Voltage Devices',form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, sensed=sensed, paced=paced, f_type=f_type, ra=ra, rv=rv)



@devices.route('/devices/crtd/<id>')
@login_required
def crtd_device(id):
    devices = CRTD.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/crtd_device.html', device=devices, page_title=devices.model_number)

@devices.route('/devices/hv', methods=['GET', 'POST'])
@login_required
def hv():
    f_type = request.args.get('f_type')
    if f_type == '1':
        form = Device_New()
        if form.validate_on_submit():
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type =f_type))
    elif f_type == '2':
        form = Devices_Change()
        if form.validate_on_submit():
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type =f_type))
    elif f_type == '3':
        form = Device_Find()
        if form.validate_on_submit():
            return redirect(url_for('devices.hv',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type = f_type))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    paced = request.args.get('paced')
    sensed = request.args.get('sensed')
    ra = request.args.get('ra')
    rv = request.args.get('rv')

    nbg = ''

    if paced and sensed:
        nbg = paced + sensed
        form.paced.data = paced
        form.sensed.data = sensed

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
    if nbg:
        #devices = devices.filter(CRTD.nbg_code.like(nbg + '%'))
        pass
    if ra:
        devices = devices.filter(HV.sense.like(ra + '%'))
        form.ra.data = ra
    if rv:
        devices = devices.filter(HV.high.like(rv + '%'))
        form.rv.data = rv

    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='HV High-Voltage Leads',form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, sensed=sensed, paced=paced, f_type=f_type, ra=ra, rv=rv)


@devices.route('/devices/hv/<id>')
@login_required
def hv_device(id):
    devices = HV.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/hv_device.html', device=devices, page_title=devices.model_number)


@devices.route('/devices/icd', methods=['GET', 'POST'])
@login_required
def icd():
    f_type = request.args.get('f_type')
    if f_type == '1':
        form = Device_New()
        if form.validate_on_submit():
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type =f_type))
    elif f_type == '2':
        form = Devices_Change()
        if form.validate_on_submit():
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type =f_type))
    elif f_type == '3':
        form = Device_Find()
        if form.validate_on_submit():
            return redirect(url_for('devices.icd',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type = f_type))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    paced = request.args.get('paced')
    sensed = request.args.get('sensed')
    ra = request.args.get('ra')
    rv = request.args.get('rv')

    nbg = ''

    if paced and sensed:
        nbg = paced + sensed
        form.paced.data = paced
        form.sensed.data = sensed
    devices = ICD.query

    if manufacturer:
        devices = devices.filter(ICD.manufacturer.like('%' + manufacturer + '%'))
        form.manufacturer.data = manufacturer
    if model_number:
        devices = devices.filter(ICD.model_number.like('%' + model_number + '%' ))
        form.model_number.data = model_number
    if device_name:
        devices = devices.filter(ICD.name.like('%' + device_name + '%' ))
        form.name.data = device_name
    if nbg:
        devices = devices.filter(ICD.nbg_code.like(nbg + '%'))
    if ra:
        devices = devices.filter(ICD.ra.like(ra + '%'))
        form.ra.data = ra
    if rv:
        devices = devices.filter(ICD.rv.like(rv + '%'))
        form.rv.data = rv

    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='ICD High-Voltage Devices',form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, sensed=sensed, paced=paced, f_type=f_type, ra=ra, rv=rv)


@devices.route('/devices/icd/<id>')
@login_required
def icd_device(id):
    devices = ICD.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/icd_device.html', device=devices, page_title=devices.model_number)

@devices.route('/devices/lv', methods=['GET', 'POST'])
@login_required
def lv():
    f_type = request.args.get('f_type')
    if f_type == '1':
        form = Device_New()
        if form.validate_on_submit():
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, f_type =f_type))
    elif f_type == '2':
        form = Devices_Change()
        if form.validate_on_submit():
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data.strip(), paced=form.paced.data, sensed=form.sensed.data, ra=form.ra.data, rv=form.rv.data, f_type =f_type))
    elif f_type == '3':
        form = Device_Find()
        if form.validate_on_submit():
            return redirect(url_for('devices.lv',manufacturer=form.manufacturer.data.strip(), model_number=form.model_number.data.strip(), device_name=form.name.data.strip(), f_type = f_type))

    page = request.args.get('page', 1, type=int)
    manufacturer = request.args.get('manufacturer')
    model_number = request.args.get('model_number')
    device_name = request.args.get('device_name')
    paced = request.args.get('paced')
    sensed = request.args.get('sensed')
    ra = request.args.get('ra')
    rv = request.args.get('rv')

    nbg = ''

    if paced and sensed:
        nbg = paced + sensed
        form.paced.data = paced
        form.sensed.data = sensed
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
    if nbg:
        #devices = devices.filter(ICD.nbg_code.like(nbg + '%'))
        pass
    if ra:
        devices = devices.filter(LV.sense.like(ra + '%'))
        form.ra.data = ra
    if rv:
        #devices = devices.filter(ICD.rv.like(rv + '%'))
        form.rv.data = rv

    devices = devices.paginate(page=page, per_page=10)
    return render_template('/Devices/Devices.html', devices=devices, page_title='LV Low-Voltage Devices',form=form, manufacturer=manufacturer, model_number=model_number, device_name=device_name, sensed=sensed, paced=paced, f_type=f_type, ra=ra, rv=rv)


@devices.route('/devices/lv/<id>')
@login_required
def lv_device(id):
    devices = LV.query.filter_by(id=id).first_or_404()
    return render_template('/Devices/lv_device.html', device=devices, page_title=devices.model_number)
