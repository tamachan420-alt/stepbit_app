from flask import Blueprint, request, jsonify, current_app, Response
import json
from backend.config import Config

bp = Blueprint('suggest', __name__, url_prefix='/api')

@bp.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()

    name = data.get("name", "あなた")
    gender = data.get("gender", "")
    age = data.get("age", "")
    type_name = data.get("type", "")
    goal = data.get("goal", "")
    mood = data.get("mood", "")

    prompt = f"""
    ユーザー情報:
    - 名前: {name}
    - 性別: {gender}
    - 年齢: {age}
    - 性格タイプ: {type_name}
    - 目標: {goal}
    - 今日の気分: {mood}

    上記をもとに、{name}さんが今日1日で達成できる小さなチャレンジを1つ提案してください。
    出力条件は以下です。
    - 日本語で回答してください。
    - 具体的で実行可能な内容にしてください。
    - チャレンジは1つだけ提案してください。
    - チャレンジはポジティブで前向きな内容にしてください。
    - チャレンジは、50字以内で出力してください。
    - チャレンジは現実的で、目標達成に少しでも近づくものにしてください。
    - チャレンジの後に、チャレンジに取り組む際の簡単なアドバイスを添えてください。
    - アドバイスの内容は200字以内でお願いします。
    - 文章は優しく、励ましの言葉で終えてください。
    出力フォーマット:
    チャレンジ: <チャレンジ内容>
    アドバイス: <アドバイス内容>
    """

    try:
        client = current_app.client
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "あなたは生活改善を支援するコーチAIです。"},
                {"role": "user", "content": prompt}
            ]
        )

        suggestion = response.output[0].content[0].text.strip()

        # ✅ jsonify → Response(json.dumps(..., ensure_ascii=False)) に変更
        return Response(
            json.dumps({"ok": True, "text": suggestion}, ensure_ascii=False),
            mimetype='application/json'
        )


    except Exception as e:
        return jsonify({"error": str(e)}), 500
