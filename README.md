# StepBit（Flask統合版）

🌱 1日1チャレンジで、少しずつ成長できるアプリ「StepBit」  
このアプリは、AIがあなたに「今日の小さなチャレンジ」を提案し、  
実行後にはやさしく励ましのコメントを返してくれます。

---

## 🌼 はじめに（小6でもわかる！）

### 🧭 このフォルダの中身
stepbit_app/
├── .env.example ← これをコピーして .env を作る
├── requirements.txt ← 必要な道具のリスト
├── backend/
│ ├── app.py ← アプリの入口
│ ├── config.py ← 設定の読み込み
│ ├── models.py ← データの形（テーブル）
│ ├── routes/ ← アプリの道（API）
│ ├── utils/db_init.py ← データベースを作る魔法
│ ├── sql/ ← データベースの設計図
│ └── db/ ← データベース本体ができる場所
├── templates/stepbit.html ← 画面（あなたのHTMLをここに入れる）
└── static/js/main.js ← 画面とAPIをつなぐ橋

---

## 🪄 1. 準備（1回だけでOK）

### ① VS Codeで開く
- ダウンロードした `stepbit_app` フォルダをデスクトップに置く  
- VS Codeでフォルダごと開く

### ② `.env` を作る
- `stepbit_app/.env.example` をコピーして、**`.env`** という名前に変える  
- 中身はそのままでOK（あとでOpenAIキーを入れます）

---

### ③ 道具を入れる（ライブラリのインストール）

#### 💻 Mac の人
```bash
cd ~/Desktop/stepbit_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#### 🪟 Windows の人（PowerShell）
cd $env:USERPROFILE\Desktop\stepbit_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## 🧱 2. データベースを作る（1行コマンド）
python backend/utils/db_init.py

## 🚀 3. アプリを起動
python -m backend.app

ブラウザで
👉 http://127.0.0.1:5000/
 を開く。
「StepBit（Flask統合版）へようこそ！」と出たら成功 🎉

## 🎨 4. HTMLを反映（フロント統合）

templates/stepbit.html に今の仮画面があります。

卒業制作.html の中身をコピーして貼り替えましょう。

その中の </body> の直前にこれがあるか確認👇
なければ追加してください：

<script src="/static/js/main.js"></script>

## 🔌 5. APIの場所（main.jsが呼び出す道）
機能	メソッド	パス	内容
チャレンジ一覧	GET	/api/challenges	チャレンジの一覧を取得
チャレンジ追加	POST	/api/challenges	新しいチャレンジを追加
AI提案	POST	/api/suggest	今日の小さなチャレンジを提案
ログ保存	POST	/api/logs	実施記録を保存
AIコメント	POST	/api/comment	実施結果に応じた励ましメッセージを返す

## 🧩 6. .env.example の中身
# OpenAI
OPENAI_API_KEY=your-openai-api-key-here

# Flask
FLASK_ENV=development
FLASK_APP=backend/app.py
SECRET_KEY=change-this-to-a-random-string

# Database (SQLite)
DATABASE_URL=sqlite:///backend/db/stepbit_db.sqlite

# App defaults
DIALECT=imabari   # imabari | matsuyama | kansai | standard


.env は コミット禁止（.gitignore済）
他のメンバーはこの .env.example をコピーして使います👇
cp .env.example .env

## 💬 7. よくあるトラブルと解決法
症状	原因	対処
画面が白い	Flaskサーバーが止まっている	ターミナルでエラーを確認
日本語が「\u305f\u307e…」になる	文字化け	対応済み（ensure_ascii=False）
No module named 'backend'	実行場所が違う	python -m backend.app で起動
APIキーなしでも動く？	大丈夫！	/api/suggest はダミー応答あり

## 👩‍💻 8. 開発チーム向けメモ
📂 Git運用

開発ブランチ：feature/ai-suggest-comment

安定ブランチ：main

PR①（APIキーなし版）：マージ待ち

PR②（APIキー対応版）：次に提出予定

🛠 コード構成（技術版）

backend/app.py : Flaskアプリ作成、Blueprint登録

backend/config.py : .env読み込み（Configクラス）

backend/routes/api_suggest.py : AI提案エンドポイント

backend/routes/api_comment.py : AIコメント生成

templates/stepbit.html : フロントUI

static/js/main.js : API通信

## 🧭 9. 次のステップ（予定）

 /api/logs に日ごとの実績保存

 提案・コメント履歴をSQLiteで管理

 「今日の達成ブロック」可視化UIの実装

 mainブランチ統合 → v0.1タグ付け
