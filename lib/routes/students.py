from flask import Blueprint, request, jsonify
from models.students import Student 

student_bp = Blueprint('student', __name__, url_prefix = '/students')

@students_bp.route('/', methods = ['GET'])
def list_students():
    students = Student.get_all()
    return jsonify([student.__dict__ for student in students])

@students_bp.route('/<int:id>', methods = ['GET'])
def find_student(id):
    student = Student.find_by_id(id)
    if student: 
        return jsonify(student.__dict__) 
    return jsonify({"error": "Student not found"}), 404

@students_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    try: 
        student = Student.create(data['name'], data['gender'], data['department'])
        return jsonify(student.__dict__), 201 
    except Exception as e: 
        return jsonify({"error": str(e)}), 400

@students_bp.router('/<int:id>', methods = ['PUT'])
def update_student(id):
    student = Student.find_by_id(id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    student.name = data.get('name', student.name)
    student.gender = data.get ('gender', student.gender)
    student.department = data.get('department', stuent.department)
    try:
        student.update()
        return jsonify(student.__dict__)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@students_bp.route('/<int:id>', methods = ['DELETE']) 
def delete_student(id):
    student = Student.find_by_id(id)     
    if student:
        student.delete()
        return jsonify({"message": f"student {id} deleted"})
    return jsonify({"error": "Student not found"}), 404      


