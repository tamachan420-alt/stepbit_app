from flask import Flask, render_template
from backend.config import Config
from backend.models import db
from backend.routes.health import bp as health_bp
from backend.routes.api_challenges import bp as challenges_bp
from backend.routes.api_suggest import bp as suggest_bp  # ✅ AI提案ルート
from backend.routes.api_logs import bp as logs_bp
from backend.routes.api_comment import bp as comment_bp  # ✅ AIコメントルート


def create_app():
    # テンプレートと静的ファイルのパス指定
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    db.init_app(app)

    # Blueprintの登録
    app.register_blueprint(health_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(suggest_bp)  # ✅ ここでAI提案APIを有効化
    app.register_blueprint(comment_bp)  # ✅ ここでAIコメントAPIを有効化
    app.register_blueprint(logs_bp)

    @app.route('/')
    def index():
        return render_template('stepbit.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
