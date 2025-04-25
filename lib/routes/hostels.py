from flask import Blueprint, request, jsonify
from models.hostels import hostel_id

hostels_bp = Blueprint, request, jsonify

@hostels_bp.route('/', methods = ['GET'])
def list_hostels():
    hostels = Hostel.get_all()
    return jsonify([vars(h) for h in hostels])

@hostels_bp.route('/<int:id>', methods = ['GET'])
def get_hostel(id):
    hostel = Hostel.find_by_id(id)
    return jsonify(vars(hostel)) if hostel else ("Hostel not found", 404)

@hostels_bp.route('/', methods = ['POST'])
def create_hostel():
    data = request.json
    try:
        hostel = Hostel.create(data['name'], data['capacity'])
        return jsonify(vars(hostel)), 201
    except Exception as e: 
        return {"error": str(e)}, 400

@hostels_bp.route('/<int:id>', methods = ['PUT'])
def update_hostel(id):
    hostel = Hostel.find_by_id(id)
    if not hostel:
        return {"error": "Hostel not found"}, 404
    data = request.json
    hostel.name = data.get("name", hostel.name)
    hostel.capacity = data.get("capacity", hostel.capacity)
    hostel.update()
    return jsonify(vars(hostel))

@hostels_bp.route('/<int:id>', methods = ['DELETE'])                          
def delete_hostel(id):
    hostel = Hostel.find_by_id(id)
    if not hostel: 
        return {"error": "Hostel not found"}, 404
    hostel.delete()
    return {"message": f"Hostel {id} deleted"}    
