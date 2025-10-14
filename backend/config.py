from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

class Config:
    
    # Flask設定
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    # データベース設定
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///backend/db/stepbit_db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI APIキー
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # 既定の方言設定
    DIALECT = os.getenv("DIALECT", "standard") # デフォルトは標準語