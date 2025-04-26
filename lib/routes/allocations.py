from flask import Blueprint, request, jsonify
from models.allocations import Allocation


allocations_bp = Blueprint('allocations', __name__, url_prefix = '/allocations')


@allocations_bp.route('/', methods = ['GET'])
def get_allocations(): 
    all_allocs = Allocation.get_all()
    data =[{
        "id": a.id,
        "student_id": a.student_id,
        "room_id": a.room_id
    } for a in all_allocs]
    return jsonify(data)

@allocations_bp.route('/create', methods=['POST'])
def allocate_student():
    data = request.json
    try: 
        allocation = Allocation.create(data['student_id'], data['room_id'])
        return jsonify({
            "id": allocation.id,
            "student_id": allocation.student_id,
            "room_id": allocation.room_id
        }), 201
    except ValueError as e: 
        return jsonify({"error": str(e)}), 400


@allocations_bp.route('/reassign', methods =['POST'])
def reassign_student():
    data = request.json
    try: 
        allocation = Allocation.reassign(data['student_id'], data['new_room_id'])
        return jsonify({
            "id": allocation.id,
            "student_id": allocation.student_id,
            "room_id": allocation.room_id
        }), 200
    except Exception as e: 
        return jsonify({"error": str(e)}), 500


