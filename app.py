from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/hospital_db'
db = SQLAlchemy(app)

# Define Database Models
class Patient(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    dob = db.Column(db.Date)
    contact_info = db.Column(db.String(100))

class Vital(db.Model):
    vital_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    blood_pressure = db.Column(db.String(20))
    heart_rate = db.Column(db.Integer)
    temperature = db.Column(db.Float)
    date_recorded = db.Column(db.Date)

class FollowUp(db.Model):
    followup_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    followup_date = db.Column(db.Date)
    notes = db.Column(db.Text)

class Delivery(db.Model):
    delivery_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    delivery_date = db.Column(db.Date)
    delivery_method = db.Column(db.String(20))
    complications = db.Column(db.Boolean)

# Routes to fetch data
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{
        'id': patient.patient_id,
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'gender': patient.gender
    } for patient in patients])

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient:
        return jsonify({
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'dob': patient.dob,
            'contact_info': patient.contact_info
        })
    return jsonify({'message': 'Patient not found'}), 404

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data['gender'],
        dob=data['dob'],
        contact_info=data['contact_info']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
