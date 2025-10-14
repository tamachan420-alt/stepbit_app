from flask import Flask, render_template
from backend.config import Config
from backend.models import db
from backend.routes.health import bp as health_bp
from backend.routes.api_challenges import bp as challenges_bp
from backend.routes.api_suggest import bp as suggest_bp
from backend.routes.api_logs import bp as logs_bp
from backend.routes.api_comment import bp as comment_bp
from openai import OpenAI
import os
from dotenv import load_dotenv

# ✅ backend の1階層上の .env を明示的に読み込む
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    db.init_app(app)

    # ✅ OpenAIクライアントをFlaskアプリに紐付け
    app.client = OpenAI(api_key=app.config["OPENAI_API_KEY"])

    # ✅ Blueprint登録
    app.register_blueprint(health_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(suggest_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(logs_bp)

    @app.route('/')
    def index():
        return render_template('stepbit.html')

    return app


if __name__ == '__main__':
    app = create_app()
    print("🔑 OpenAI API KEY (masked):", str(app.config["OPENAI_API_KEY"])[:10] + "******")  # ✅ ここに移動
    app.run(debug=True)
