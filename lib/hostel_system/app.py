from flask import Flask
from routes.students import students_bp
from routes.hostels import hostels_bp
from routes.rooms import rooms_bp
from routes.allocations import allocations_bp


app = Flask(__name__)


# Register all Blueprints
app.register_blueprint(allocations_bp)
app.register_blueprint(students_bp)
app.register_blueprint(rooms_bp)
app.register_blueprint(hostels_bp)

if __name__ == '__main__':
    app.run(debug=True)