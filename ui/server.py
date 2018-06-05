from flask import Flask
from werkzeug.serving import run_simple

from blueprints.home_blueprint import home_blueprint
from core.configurations.http import SECRET_KEY, PORT, HOST
from data.db_provider_factory import DbProviderFactory

db_provider = DbProviderFactory.get_instance()

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Registering the blueprints
app.register_blueprint(home_blueprint, url_prefix='/')

if __name__ == '__main__':
    run_simple(HOST, PORT, app, use_debugger=True, use_reloader=True, use_evalex=True)
