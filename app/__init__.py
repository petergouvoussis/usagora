import dash
from flask import Flask
from flask_login import login_required

def create_app():

    from config import ConfigSetup

    server = Flask(__name__)
    server.config.from_object(ConfigSetup)

    from app.dashapps.stocks.layout import layout as layout_stocks
    from app.dashapps.stocks.callbacks import register_callbacks as register_callbacks_stocks
    register_dashapp(server, '/stocks/', layout_stocks, register_callbacks_stocks)

    from app.dashapps.options.layout import layout as layout_options
    from app.dashapps.options.callbacks import register_callbacks as register_callbacks_options
    register_dashapp(server, '/options/', layout_options, register_callbacks_options)

    from app.dashapps.financials.layout import layout as layout_financials
    from app.dashapps.financials.callbacks import register_callbacks as register_callbacks_financials
    register_dashapp(server, '/financials/', layout_financials, register_callbacks_financials)

    register_extensions(server)
    register_blueprints(server)

    return server

def register_dashapp(app, base_pathname, layout, register_callbacks_function):

    dashapp = dash.Dash(__name__, server = app, url_base_pathname=f'{base_pathname}', assets_folder = 'dashapps/assets')

    with app.app_context():

        dashapp.layout = layout
        register_callbacks_function(dashapp)

    dash_login_required(dashapp)

def dash_login_required(app):

    for view_func in app.server.view_functions:
        if view_func.startswith(app.config.url_base_pathname):
            app.server.view_functions[view_func] = login_required(app.server.view_functions[view_func])

def register_extensions(server):

    from app.extensions import db, login_manager, bcrypt
    from app.models import User

    db.init_app(server)
    bcrypt.init_app(server)
    login_manager.init_app(server)
    login_manager.login_view = 'main.login'

    with server.app_context():
        db.create_all()

def register_blueprints(server):

    from app.routes import blueprint

    server.register_blueprint(blueprint)
