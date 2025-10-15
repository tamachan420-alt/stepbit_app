from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# ベースディレクトリ（backendフォルダの絶対パス）を取得
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask設定
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    # データベース設定（絶対パス指定に変更）
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'db', 'stepbit_db.sqlite')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI APIキー
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # 既定の方言設定
    DIALECT = os.getenv("DIALECT", "standard")  # デフォルトは標準語
