from cardiacpedia.models import *
import pandas as pd

def ipg():
    df = pd.read_csv('/Devices/IPG.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = IPG(
        manufacturer=row['Manufacturer'],
        model_number=row['Model Number'],
        name=row['Name'],
        nbg_code=row['NBG Code'],
        x_ray=row['X-ray/Serial ID'],
        ra=row['Sense / Pace Connector RA'],
        rv=row['Sense / Pace Connector RV'],
        detach=row['Detach Tools'],
        n_bos=row['Non MAG Rate BOS'],
        n_rrt=row['Non MAG Rate RRT/EOS'],
        m_bos=row['MAG Rate BOS'],
        m_rrt=row['MAG Rate RRT/EOS'],
        rrt_behaviour=row['RRT/EOS Behavior'],
        rrt_longevity=row['RRT/EOS Longetivity'],
        )
        db.session.add(device)
    db.session.commit()
    print(IPG.query.all()[:10])

def crtp():
    df = pd.read_csv('Devices/CRTP.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = CRTP(
        manufacturer=row['Manufacturer'],
        model_number=row['Model Number'],
        name=row['Model Name'],
        nbg_code=row['NBG Code'],
        x_ray=row['X-ray ID'],
        ra=row['Sense/Pace Connectors RA'],
        la=row['Sense/Pace Connectors LA'],
        rv=row['Sense/Pace Connectors RV'],
        lv=row['Sense/Pace Connectors LV'],
        detach=row['Detach Tool'],
        n_bol=row['Non MAG Rate BOL'],
        n_eri=row['Non MAG Rate ERI/EOL'],
        m_bol=row['MAG Rate BOL'],
        m_eri=row['MAG Rate ERI/EOL'],
        eri_behaviour=row['ERI EOL Behavior'],
        longevity=row['Longetivity'],
        )
        db.session.add(device)
    db.session.commit()
    print(CRTP.query.all()[:10])

def icd():
    df = pd.read_csv('Devices/ICD.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = ICD(
        manufacturer=row['Manufacturer'],
        model_number=row['Model Number'],
        name=row['Model Name'],
        nbg_code=row['NBD Code'],
        x_ray=row['X-ray ID'],
        serial=row['Serial ID'],
        ra=row['Connectors RA'],
        rv=row['Connectors RV'],
        hv=row['Connectors HV'],
        detach=row['Detach Tool'],
        wave=row['HV Waveform'],
        replacement=row['Replacement Indicator'],
        )
        db.session.add(device)
    db.session.commit()
    print(ICD.query.all()[:10])

def CRTD_m():
    df = pd.read_csv('Devices/CRTD.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = CRTD(
        manufacturer=row['Manufacturer'],
        model_number=row['Model Number'],
        name=row['Model Name'],
        nbg_code=row['NBD Code'],
        x_ray=row['X-ray ID'],
        serial=row['Serial ID'],
        ra=row['Connectors RA'],
        rv=row['Connectors RV'],
        lv=row['Connectors LV'],
        hv=row['Connectors HV'],
        detach=row['Detach Tool'],
        wave=row['HV Waveform'],
        replacement=row['Replacement Indicator'],
        )
        db.session.add(device)
    db.session.commit()
    print(CRTD.query.all()[:10])

def LV_m():
    df = pd.read_csv('Devices/LV.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = LV(
        manufacturer=row['Manufacturer'],
        model_number=row['Model Number'],
        name=row['Model Name'],
        serial=row['Serial ID'],
        sense=row['Connectors Sense/Pace'],
        polarity=row['Polarity'],
        fixation=row['Fixation'],
        placement=row['Placement'],
        insulation=row['Outer Insulation'],
        location=row['Location'],
        )
        db.session.add(device)
    db.session.commit()
    print(LV.query.all()[:10])


def HV_m():
    df = pd.read_csv('Devices/HV.csv', encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        device = HV(
        manufacturer=row['Manufacturer'],
        model_number=row['Model Number'],
        name=row['Name'],
        serial=row['Serial ID'],
        sense=row['Connectors Sense/Pace'],
        high=row['High Voltage'],
        sensing=row['Sensing Configurations'],
        lead=row['Lead Polarity'],
        placement=row['Placement'],
        fixation=row['Fixation'],
        insulation=row['Insultation'],
        )
        db.session.add(device)
    db.session.commit()
    print(HV.query.all()[:10])






















if __name__ == '__main__':
    HV_m()
