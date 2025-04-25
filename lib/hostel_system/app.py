from flask import flask
from routes.allocations import allocatins_bp

app = Flask(__name__)
app.register_blueprint(allcotions_bp)

if __name__ == '__main__':
    app.run(debug=True)