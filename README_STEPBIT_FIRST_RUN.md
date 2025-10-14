# StepBit（Flask統合版）最初の動かし方
（小6でもわかるように・超ていねい手順）

## 0. フォルダの中身（だいじな場所）
```
stepbit_app/
├── .env.example          ← これをコピーして .env を作る
├── requirements.txt      ← 必要な道具のリスト
├── backend/
│   ├── app.py            ← アプリの入口
│   ├── config.py         ← 設定の読み込み
│   ├── models.py         ← データの形（テーブル）
│   ├── routes/           ← アプリの道（API）
│   ├── utils/db_init.py  ← データベースを作る魔法
│   ├── sql/              ← データベースの設計図
│   └── db/               ← データベース本体ができる場所
├── templates/stepbit.html ← 画面（あなたのHTMLをここに入れる）
└── static/js/main.js     ← 画面とAPIをつなぐ橋
```

## 1. 準備（1回だけ）
### 1-1. フォルダを開く
- ダウンロードした `stepbit_app` をデスクトップに置く
- VS Code で `stepbit_app` を開く

### 1-2. .env を作る
- `stepbit_app/.env.example` をコピーして **`.env`** という名前にする（中身はそのままでOK）

### 1-3. 道具を入れる（ライブラリのインストール）
**Mac の人：**
```bash
cd ~/Desktop/stepbit_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**Windows の人（PowerShell）：**
```powershell
cd $env:USERPROFILE\Desktop\stepbit_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 2. データベースを作る（ボタン1つ分の操作）
```bash
python backend/utils/db_init.py
```
終わると `backend/db/stepbit_db.sqlite` ができます。

## 3. アプリを起動する
```bash
python backend/app.py
```
ブラウザで `http://127.0.0.1:5000/` を開きます。  
「StepBit（Flask統合版）へようこそ！」と出たら成功 🎉

## 4. あなたのHTML（stepbit_prototype.html）に差し替える
- 今は `templates/stepbit.html` に**仮の画面**が入っています。
- あなたの `frontend_prototype/stepbit_prototype.html` の**中身**を、`templates/stepbit.html` に**貼り替えてください**。
- 1点だけ：`</body>` の直前に以下があるか確認。なければ入れてください。
```html
<script src="/static/js/main.js"></script>
```

## 5. APIの場所（main.jsが使う道）
- 一覧：`GET /api/challenges`
- 追加：`POST /api/challenges`
- AI提案：`POST /api/suggest`
- ログ保存：`POST /api/logs`

## 6. 困ったときは
- 画面が白い → ターミナルのエラーを見る
- OpenAIキーなし → 大丈夫。`/api/suggest` はダミー回答が返ります
- DBがない → 「2. データベースを作る」を実行

がんばっていきましょう！
