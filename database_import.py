from cardiacpedia.models import db, IPG
import pandas as pd


if __name__ == '__main__':

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
