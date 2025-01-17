from flask import Flask, jsonify, request # type: ignore
app = Flask(__name__)

# use decorators to route to the GET request
@app.route("/get/", methods=['GET'])
def handle_get():
    return jsonify({"message": "This is a GET request"}) 

# Route to POST requests
@app.route("/post/", methods=['POST'])
def handle_post():
    return jsonify({"message": "This is a POST request"}) 

# Route to multiply a number by 2
@app.route("/multiply/<int:num>", methods=['GET'])
def multiply(num):
    return jsonify({"result": num * 2}) 

# post route for salary computation
@app.route("/salary/", methods=['POST'])
def salary():
    data = request.get_json()
    required_fields = ['salary', 'bonus', 'taxes']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        salary = float(data['salary'])
        bonus = float(data['bonus'])
        taxes = float(data['taxes'])
    except ValueError:
        return jsonify({"error": "Expected numbers, got strings"}), 400

    # compute result
    result = salary + bonus - taxes
    return jsonify({"result": result}) 

if __name__ == "__main__":
    app.run(debug=True)