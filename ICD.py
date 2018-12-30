from cardiacpedia.models import db, ICD
import pandas as pd


if __name__ == '__main__':

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
        hv=row['HV Waveform'],
        replacement=row['Replacement Indicator'],
        )
        db.session.add(device)
    db.session.commit()
    print(ICD.query.all()[:10])
