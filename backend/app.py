from flask import Flask, render_template
from backend.config import Config
from backend.models import db
from backend.routes.health import bp as health_bp
from backend.routes.api_challenges import bp as challenges_bp
from backend.routes.api_suggest import bp as suggest_bp
from backend.routes.api_logs import bp as logs_bp

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(suggest_bp)
    app.register_blueprint(logs_bp)

    @app.route('/')
    def index():
        return render_template('stepbit.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
