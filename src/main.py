"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import json
from flask import Flask, request, jsonify, url_for, make_response
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Client
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/clients', methods=['POST', 'GET'])
@app.route('/clients/<client_id>', methods=['DELETE', 'PUT'])
def handle_clients(client_id=0):
    headers = {
        "Content-Type": "application/json"
    }

    if request.method == "POST":
        print("creating client")
        client = request.json
        print(request.json)
        new_client = Client(client["name"], client["lastName"], client["company"], client["position"], client["email"], client["phone"], client["extraPhone"], client["sector"], client["city"], client["country"], client["linkedin"], client["source"], client["observations"])
        db.session.add(new_client)
        db.session.commit()
        response_body = {
            "status": "HTTP_200_OK. Ok"
        }
        status_code = 200

    elif request.method == "GET":
        user_client_list = Client.query.all()
        response_body = []
        for client in user_client_list:
            response_body.append(client.serialize())
        status_code = 200

    elif request.method == "DELETE":
        Client.query.filter_by(id=client_id).delete()
        db.session.commit()
        response_body = {
            "result": "ok",
            "status": "HTTP_204_NO_CONTENT. User and tasks deleted."
        }
        status_code = 204

    
    return make_response(
        json.dumps(response_body),
        status_code,
        headers
    )

@app.route('/opportunitys', methods=['POST', 'GET'])
@app.route('/opportunitys/<opportunity_id>', methods=['DELETE', 'PUT'])
def handle_opportunitys(opportunity_id=0):
    headers = {
        "Content-Type": "application/json"
    }

    if request.method == "POST":
        print("creating opportunity")
        opportunity = request.json
        print(request.json)
        new_opportunity = Opportunity(opportunity["project"], opportunity["projectDescription"], opportunity["cost"], opportunity["time"], opportunity["reach"])
        db.session.add(new_opportunity)
        db.session.commit()
        response_body = {
            "status": "HTTP_200_OK. Ok"
        }
        status_code = 200
    
    return make_response(
    json.dumps(response_body),
    status_code,
    headers
    )

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

