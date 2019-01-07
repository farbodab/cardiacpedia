from cardiacpedia import app
from cardiacpedia.models import *
import datetime


if __name__ == '__main__':
    #Create 'admin@example.com' user with 'Admin' and 'Agent' roles
    if not User.query.filter(User.email == 'farbod.ab@hotmail.ca').first():
        user = User(
            email='farbod.ab@hotmail.ca',
            password='Kalimdor1996',
            access='3'
        )
        db.session.add(user)
        db.session.commit()
    app.run(debug=True)
