from cardiacpedia.models import db, CRTP
import pandas as pd


if __name__ == '__main__':

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
