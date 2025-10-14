from flask import Blueprint, jsonify, request
from backend.models import db, Log

bp = Blueprint('logs', __name__)

@bp.route('/api/logs', methods=['POST'])
def add_log():
    data = request.get_json(force=True)
    entry = Log(
        challenge_id=data.get('challenge_id'),
        progress=data.get('progress',''),
        created_at=data.get('created_at','')
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify({'ok': True, 'id': entry.id}), 201
