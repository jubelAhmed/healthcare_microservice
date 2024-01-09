from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint for fetching doctor names
@app.route('/doctors', methods=['GET'])
def get_doctors():
    # Dummy doctor names
    doctors = doctor_list = [
    {"name": "Dr. Smith", "doctor_id": 1001, "expertise": "Cardiology"},
    {"name": "Dr. Johnson", "doctor_id": 1002, "expertise": "Pediatrics"},
    {"name": "Dr. Davis", "doctor_id": 1003, "expertise": "Orthopedics"},
    {"name": "Dr. Miller", "doctor_id": 1004, "expertise": "Oncology"},
    {"name": "Dr. Wilson", "doctor_id": 1005, "expertise": "Neurology"}
]

    return jsonify(doctors)
    #return('hello')

if __name__ == '__main__':
    app.run(debug=True)
