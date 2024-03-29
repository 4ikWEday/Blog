from flask import Flask
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=None)
    app.config.from_mapping(
        SECRET_KEY = "gghtcv",
        DATABASE=os.path.join(app.instance_path, 'mysite.sqlite')
    )


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    


    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    return app

