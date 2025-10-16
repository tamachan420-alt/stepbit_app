import os
from flask import Flask, render_template
from dotenv import load_dotenv
from openai import OpenAI
from backend.config import Config

# 各モジュール（ルート）
from backend.routes.api_suggest import bp as suggest_bp
from backend.routes.api_comment import bp as comment_bp

# .env を 1階層上から読み込む
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(Config)

    # ✅ OpenAI クライアントの初期化
    app.client = OpenAI(api_key=app.config["OPENAI_API_KEY"])

    # ✅ Blueprint 登録
    app.register_blueprint(suggest_bp)
    app.register_blueprint(comment_bp)

    # テスト用ルート（ブラウザ確認用）
    @app.route("/")
    def index():
        return render_template("stepbit.html")

    return app
