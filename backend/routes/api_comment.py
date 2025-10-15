from flask import Blueprint, request, jsonify, current_app, Response
import json

bp = Blueprint('comment', __name__, url_prefix='/api')

@bp.route('/comment', methods=['POST'])
def comment():
    data = request.get_json()

    # --- ユーザー情報 ---
    name = data.get("name", "あなた")
    gender = data.get("gender", "")
    age = data.get("age", "")
    type_name = data.get("type", "")
    goal = data.get("goal", "")
    mood = data.get("mood", "")
    result = data.get("result", "")
    dialect = data.get("dialect", "standard")  # ← 方言モード

    # --- 方言設定 ---
    if dialect in ["imabari", "ehime"]:
        style = "伊予弁で、あたたかく励ます感じで話してください。"
    elif dialect in ["matsuyama"]:
        style = "松山弁で、やさしくフレンドリーに話してください。"
    elif dialect in ["kansai", "osaka"]:
        style = "関西弁で、フレンドリーにツッコミ混じりでコメントしてください。"
    else:
        style = "標準語で、優しく励ます感じで話してください。"

    # --- プロンプト生成 ---
    prompt = f"""
    ユーザー情報:
    - 名前: {name}
    - 性別: {gender}
    - 年齢: {age}
    - 性格タイプ: {type_name}
    - 目標: {goal}
    - 今日の気分: {mood}
    - 実施結果: {result}

    条件:
    - {style}
    - 文字数は60文字以内。
    - 絵文字を1〜2個入れてもよい。

    {name}さんへのコメントを出力してください。
    """

    try:
        # ✅ Flaskアプリに登録済みのOpenAIクライアントを取得
        client = current_app.client

        # ✅ GPT-4oの新API（responses）を使用
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "あなたは利用者を優しく励ますコーチAIです。"},
                {"role": "user", "content": prompt}
            ]
        )

        comment_text = response.output[0].content[0].text.strip()
        
        return Response(
            json.dumps({"comment": comment_text}, ensure_ascii=False),
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "API is alive!"})
