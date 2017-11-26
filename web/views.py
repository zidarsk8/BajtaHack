"""Bajta hack views module."""

import flask


def init_views(app):
    """Initialize all views.

    Views should be initialized in a function to prevent dependencies between
    module imports.

    Args:
        app: Flask App.
    """
    # pylint: disable=unused-variable
    @app.route('/')
    def index():
        return flask.render_template("app.html")

    @app.route('/status')
    def status():
        test_cases = [{
            "value": True,
            "id": 1,
            "mode": "manual",
        }]

        response = app.response_class(
            response=flask.json.dumps(test_cases),
            status=200,
            mimetype='application/json'
        )
        return response
