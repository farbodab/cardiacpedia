from cardiacpedia.models import *
import pandas as pd

def ipg():
    df = pd.read_csv('Devices/IPG.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = IPG(
        manufacturer=string(row['Manufacturer']),
        model_number=string(row['Model Number']),
        name=string(row['Name']),
        nbg_code=string(row['NBG Code']),
        x_ray=string(row['X-ray/Serial ID']),
        ra=string(row['Sense / Pace Connector RA']),
        rv=string(row['Sense / Pace Connector RV']),
        detach=string(row['Detach Tools']),
        n_bos=string(row['Non MAG Rate BOS']),
        n_rrt=string(row['Non MAG Rate RRT/EOS']),
        m_bos=string(row['MAG Rate BOS']),
        m_rrt=string(row['MAG Rate RRT/EOS']),
        rrt_behaviour=string(row['RRT/EOS Behavior']),
        rrt_longevity=string(row['RRT/EOS Longetivity']),
        )
        db.session.add(device)
    db.session.commit()
    print(IPG.query.all()[:10])

def crtp():
    df = pd.read_csv('Devices/CRTP.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = CRTP(
        manufacturer=string(row['Manufacturer']),
        model_number=string(row['Model Number']),
        name=string(row['Model Name']),
        nbg_code=string(row['NBG Code']),
        x_ray=string(row['X-ray ID']),
        ra=string(row['Sense/Pace Connectors RA']),
        la=string(row['Sense/Pace Connectors LA']),
        rv=string(row['Sense/Pace Connectors RV']),
        lv=string(row['Sense/Pace Connectors LV']),
        detach=string(row['Detach Tool']),
        n_bol=string(row['Non MAG Rate BOL']),
        n_eri=string(row['Non MAG Rate ERI/EOL']),
        m_bol=string(row['MAG Rate BOL']),
        m_eri=string(row['MAG Rate ERI/EOL']),
        eri_behaviour=string(row['ERI EOL Behavior']),
        longevity=string(row['Longetivity']),
        )
        db.session.add(device)
    db.session.commit()
    print(CRTP.query.all()[:10])

def icd():
    df = pd.read_csv('Devices/ICD.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = ICD(
        manufacturer=string(row['Manufacturer']),
        model_number=string(row['Model Number']),
        name=string(row['Model Name']),
        nbg_code=string(row['NBD Code']),
        x_ray=string(row['X-ray ID']),
        serial=string(row['Serial ID']),
        ra=string(row['Connectors RA']),
        rv=string(row['Connectors RV']),
        hv=string(row['Connectors HV']),
        detach=string(row['Detach Tool']),
        wave=string(row['HV Waveform']),
        replacement=string(row['Replacement Indicator']),
        )
        db.session.add(device)
    db.session.commit()
    print(ICD.query.all()[:10])

def CRTD_m():
    df = pd.read_csv('Devices/CRTD.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = CRTD(
        manufacturer=string(row['Manufacturer']),
        model_number=string(row['Model Number']),
        name=string(row['Model Name']),
        nbg_code=string(row['NBD Code']),
        x_ray=string(row['X-ray ID']),
        serial=string(row['Serial ID']),
        ra=string(row['Connectors RA']),
        rv=string(row['Connectors RV']),
        lv=string(row['Connectors LV']),
        hv=string(row['Connectors HV']),
        detach=string(row['Detach Tool']),
        wave=string(row['HV Waveform']),
        replacement=string(row['Replacement Indicator']),
        )
        db.session.add(device)
    db.session.commit()
    print(CRTD.query.all()[:10])

def LV_m():
    df = pd.read_csv('Devices/LV.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = LV(
        manufacturer=string(row['Manufacturer']),
        model_number=string(row['Model Number']),
        name=string(row['Model Name']),
        serial=string(row['Serial ID']),
        sense=string(row['Connectors Sense/Pace']),
        polarity=string(row['Polarity']),
        fixation=string(row['Fixation']),
        placement=string(row['Placement']),
        insulation=string(row['Outer Insulation']),
        location=string(row['Location']),
        )
        db.session.add(device)
    db.session.commit()
    print(LV.query.all()[:10])


def HV_m():
    df = pd.read_csv('Devices/HV.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = HV(
        manufacturer=string(row['Manufacturer']),
        model_number=string(row['Model Number']),
        name=string(row['Name']),
        serial=string(row['Serial ID']),
        sense=string(row['Connectors Sense/Pace']),
        high=string(row['High Voltage']),
        sensing=string(row['Sensing Configurations']),
        lead=string(row['Lead Polarity']),
        placement=string(row['Placement']),
        fixation=string(row['Fixation']),
        insulation=string(row['Insultation']),
        )
        db.session.add(device)
    db.session.commit()
    print(HV.query.all()[:10])


if __name__ == '__main__':
    ipg()
    crtp()
    icd()
    CRTD_m()
    LV_m()
    HV_m()
