from datetime import datetime
from src import create_app
from src.db import init_db, db_session
from src.models import TourGroups, Tags, Price

app = create_app()


@app.teardown_request
def session_clear(exception):
    db_session.remove()


@app.before_first_request
def seed():
    init_db()
    Tags_counts = Tags.query.filter().count()
    if Tags_counts == 0:
        db_session.add(TourGroups(name="914的黑團子", place="台北", price="1"))
        db_session.add(Tags(name="企業包團"))
        db_session.add(Price(price=3380, startDate=datetime(2020, 11, 12)))
        db_session.commit()


if __name__ == '__main__':
    app.run()
