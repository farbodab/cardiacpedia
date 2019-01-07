from cardiacpedia.models import *
import pandas as pd

def ipg():
    df = pd.read_csv('Devices/IPG.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = IPG(
        manufacturer=str(row['Manufacturer']),
        model_number=str(row['Model Number']),
        name=str(row['Name']),
        nbg_code=str(row['NBG Code']),
        x_ray=str(row['X-ray/Serial ID']),
        ra=str(row['Sense / Pace Connector RA']),
        rv=str(row['Sense / Pace Connector RV']),
        detach=str(row['Detach Tools']),
        n_bos=str(row['Non MAG Rate BOS']),
        n_rrt=str(row['Non MAG Rate RRT/EOS']),
        m_bos=str(row['MAG Rate BOS']),
        m_rrt=str(row['MAG Rate RRT/EOS']),
        rrt_behaviour=str(row['RRT/EOS Behavior']),
        rrt_longevity=str(row['RRT/EOS Longetivity']),
        )
        db.session.add(device)
    db.session.commit()
    print(IPG.query.all()[:10])

def crtp():
    df = pd.read_csv('Devices/CRTP.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = CRTP(
        manufacturer=str(row['Manufacturer']),
        model_number=str(row['Model Number']),
        name=str(row['Model Name']),
        nbg_code=str(row['NBG Code']),
        x_ray=str(row['X-ray ID']),
        ra=str(row['Sense/Pace Connectors RA']),
        la=str(row['Sense/Pace Connectors LA']),
        rv=str(row['Sense/Pace Connectors RV']),
        lv=str(row['Sense/Pace Connectors LV']),
        detach=str(row['Detach Tool']),
        n_bol=str(row['Non MAG Rate BOL']),
        n_eri=str(row['Non MAG Rate ERI/EOL']),
        m_bol=str(row['MAG Rate BOL']),
        m_eri=str(row['MAG Rate ERI/EOL']),
        eri_behaviour=str(row['ERI EOL Behavior']),
        longevity=str(row['Longetivity']),
        )
        db.session.add(device)
    db.session.commit()
    print(CRTP.query.all()[:10])

def icd():
    df = pd.read_csv('Devices/ICD.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = ICD(
        manufacturer=str(row['Manufacturer']),
        model_number=str(row['Model Number']),
        name=str(row['Model Name']),
        nbg_code=str(row['NBD Code']),
        x_ray=str(row['X-ray ID']),
        serial=str(row['Serial ID']),
        ra=str(row['Connectors RA']),
        rv=str(row['Connectors RV']),
        hv=str(row['Connectors HV']),
        detach=str(row['Detach Tool']),
        wave=str(row['HV Waveform']),
        replacement=str(row['Replacement Indicator']),
        )
        db.session.add(device)
    db.session.commit()
    print(ICD.query.all()[:10])

def CRTD_m():
    df = pd.read_csv('Devices/CRTD.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = CRTD(
        manufacturer=str(row['Manufacturer']),
        model_number=str(row['Model Number']),
        name=str(row['Model Name']),
        nbg_code=str(row['NBD Code']),
        x_ray=str(row['X-ray ID']),
        serial=str(row['Serial ID']),
        ra=str(row['Connectors RA']),
        rv=str(row['Connectors RV']),
        lv=str(row['Connectors LV']),
        hv=str(row['Connectors HV']),
        detach=str(row['Detach Tool']),
        wave=str(row['HV Waveform']),
        replacement=str(row['Replacement Indicator']),
        )
        db.session.add(device)
    db.session.commit()
    print(CRTD.query.all()[:10])

def LV_m():
    df = pd.read_csv('Devices/LV.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = LV(
        manufacturer=str(row['Manufacturer']),
        model_number=str(row['Model Number']),
        name=str(row['Model Name']),
        serial=str(row['Serial ID']),
        sense=str(row['Connectors Sense/Pace']),
        polarity=str(row['Polarity']),
        fixation=str(row['Fixation']),
        placement=str(row['Placement']),
        insulation=str(row['Outer Insulation']),
        location=str(row['Location']),
        )
        db.session.add(device)
    db.session.commit()
    print(LV.query.all()[:10])


def HV_m():
    df = pd.read_csv('Devices/HV.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = HV(
        manufacturer=str(row['Manufacturer']),
        model_number=str(row['Model Number']),
        name=str(row['Name']),
        serial=str(row['Serial ID']),
        sense=str(row['Connectors Sense/Pace']),
        high=str(row['High Voltage']),
        sensing=str(row['Sensing Configurations']),
        lead=str(row['Lead Polarity']),
        placement=str(row['Placement']),
        fixation=str(row['Fixation']),
        insulation=str(row['Insultation']),
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
