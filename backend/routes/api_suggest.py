from flask import Blueprint, jsonify, request
import os

bp = Blueprint('suggest', __name__)

@bp.route('/api/suggest', methods=['POST'])
def suggest():
    data = request.get_json(force=True) or {}
    mood = data.get('mood', 'ふつう')
    api_key = os.getenv('OPENAI_API_KEY','')
    if not api_key:
        return jsonify({'suggestion': f'今日は「{mood}」の気分だね。5分だけストレッチしてみよう！'})
    try:
        import openai
        openai.api_key = api_key
        prompt = f'ユーザーの今日の気分は「{mood}」。やる気が出る小さなチャレンジを1つだけ短く日本語で提案してください。'
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'system','content':'StepBitのAIアシスタント'},{'role':'user','content':prompt}],
            temperature=0.7, max_tokens=120
        )
        suggestion = resp['choices'][0]['message']['content']
        return jsonify({'suggestion': suggestion})
    except Exception:
        return jsonify({'suggestion': f'（代替提案）まず深呼吸3回。水を一杯飲んで、1つだけ簡単なタスクに着手しよう。'})
