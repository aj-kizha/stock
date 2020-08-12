from flask import Flask
from restplus.apis import api



def create_app():
    print("creating app")
    app = Flask(__name__)
    load_config(app)
    api.init_app(app)
    return app


def load_config(app):
    app.config.from_object('config.app_conf_local')

app = create_app()
