from flask import Blueprint, request, jsonify
from openai import OpenAI
from backend.config import Config

bp = Blueprint('comment', __name__, url_prefix='/api')
client = OpenAI(api_key=Config.OPENAI_API_KEY)

@bp.route('/comment', methods=['POST'])
def comment():
    data = request.get_json()

    # ユーザー情報
    name = data.get("name", "あなた")
    gender = data.get("gender", "")
    age = data.get("age", "")
    type_name = data.get("type", "")
    goal = data.get("goal", "")
    mood = data.get("mood", "")
    result = data.get("result", "")  # ← 実施結果（やった・ややできた・できなかった）
    dialect = data.get("dialect", "standard")  # ← 方言モード

    # 方言設定
    if dialect == "ehime":
        style = "伊予弁で、あたたかく励ます感じで話してください。"
    elif dialect == "osaka":
        style = "関西弁で、フレンドリーにツッコミ混じりでコメントしてください。"
    else:
        style = "標準語で、優しく励ます感じで話してください。"

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
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは利用者を優しく励ますコーチAIです。"},
                {"role": "user", "content": prompt}
            ]
        )
        comment_text = response.choices[0].message.content.strip()
        return jsonify({"comment": comment_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
