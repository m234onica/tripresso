import werkzeug.datastructures
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
        db_session.add(TourGroups(name="914的黑團子", place="台北"))
        db_session.add(Tags(name="企業包團"))
        db_session.add(Price(groupId="1", startDate=datetime(2020, 11, 12)))
        db_session.commit()


def main(request):
    with app.app_context():
        headers = werkzeug.datastructures.Headers()
        for key, value in request.headers.items():
            headers.add(key, value)
        with app.test_request_context(method=request.method, base_url=request.base_url, path=request.path, query_string=request.query_string, headers=headers, data=request.data):
            try:
                rv = app.preprocess_request()
                if rv is None:
                    rv = app.dispatch_request()
            except Exception as e:
                rv = app.handle_user_exception(e)
            response = app.make_response(rv)
            return app.process_response(response)
