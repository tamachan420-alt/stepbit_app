from flask import Blueprint, jsonify, request
from backend.models import db, Challenge

bp = Blueprint('challenges', __name__)

@bp.route('/api/challenges', methods=['GET'])
def list_challenges():
    items = Challenge.query.order_by(Challenge.id.desc()).all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/api/challenges', methods=['POST'])
def add_challenge():
    data = request.get_json(force=True)
    new_item = Challenge(
        title=data.get('title','Untitled'),
        date=data.get('date'),
        status=data.get('status','incomplete')
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'ok': True, 'id': new_item.id}), 201
