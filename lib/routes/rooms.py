from flask import Blueprint, request, jsonify
from models.rooms import Room 

rooms_bp = Blueprint('rooms', __name__, url_prefix = '/rooms')

@rooms_bp.route('/', methods = ['GET'])
def list_rooms():
    rooms = Room.get_all()
    return jsonify([vars(r) for r in rooms])

@rooms_bp.route('/<int:id>', methods = ['GET'])
def get_room(id):
    room = Room.find_by_id(id)
    return jsonify(vars(room)) if room else ("Room not found", 404)

@rooms_bp.route('/', methods = ['POST'])
def create_room():
    data = request.json
    try: 
        room = Room.create(data['room_number'], data['capacity'], data['hostel_id'])
        return jsonify(vars(room)), 201
    except Exception as e:
        return {"error": str(e)}, 400

@rooms_bp.route('/<int:id>', methods = ['PUT'])
def update_room(id):
    room = Room.find_by_id(id) 
    if not room: 
        return {"error": "Room not found"}, 404
    data = request.json
    room.room_number = data.get('room_number', room.room_number)
    room.capacity = data.get('capacity', room.capacity)
    room.hostel_id = data.get('hostel_id', room.hostel_id)
    room.update()
    return jsonify(vars(room))

@rooms_bp.route('/<int:id>', methods = ['DELETE'])
def delete_room(id):
    room = Room.find_by_id(id)
    if not room: 
        return {"error": "Room not found"}, 404
    room.delete()
    return {"message": f"Room {id} deleted"}       
