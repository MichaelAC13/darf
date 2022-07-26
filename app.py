
from flask import Flask,request,jsonify, send_file
from flask_cors import CORS, cross_origin
from darf import darf

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "*.*"}})

# ROTAS

@app.route("/",  methods=['POST']) 
@cross_origin()
def home():
    return jsonify({
        "api": "API FLASK",
        "version": "1.0.0"
    })

@app.route("/darfs", methods=['POST']) 
@cross_origin()
def darfs(): 
    req = request.get_json()
    isert = darf.insertdata(req)
    print(isert)
    return send_file(isert, mimetype='application/zip')
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)