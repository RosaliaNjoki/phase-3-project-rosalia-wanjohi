from flask import flask
from routes.allocations import allocations_bp
from routes.students import student_bp

app = Flask(__name__)
app.register_blueprint(allocations_bp)
app.register_blueprint(student_bp)

if __name__ == '__main__':
    app.run(debug=True)