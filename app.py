from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, your Appointment Booking System is live!"

if __name__ == "__main__":
    app.run(debug=True)

# Sample in-memory data store
appointments = []

# Route to view all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

# Route to add a new appointment
@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()  # Get the data sent in the request
    appointment = {
        'name': data['name'],
        'date': data['date'],
        'time': data['time'],
        'service': data['service']
    }
    appointments.append(appointment)  # Add the new appointment to the list
    return jsonify({'message': 'Appointment added successfully!', 'appointment': appointment}), 201

if __name__ == '__main__':
    app.run(debug=True)    