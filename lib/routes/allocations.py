from flask import Flask, request, jsonify
from models.allocations import Allocation
from models.__init__ import CONN

app = Flask(__name__)


@app.route('/allocations', methods = ['Get'])
def get_allocations(): 
    all_allocs = Allocation.get_all()
    data =[{
        "id": a.id,
        "student_id": a.student_id,
        "room_id": a.room_id
    } for a in all_allocs]
    return jsonify(data)

@app.route('/allocte', methods=['POST'])
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


@app.route('/reassign', methods =['POST'])
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


if __name__ == "__main__":
    app.run(debug=True)