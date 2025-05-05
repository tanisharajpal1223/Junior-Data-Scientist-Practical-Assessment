-- Patients Table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    dob DATE,
    contact_info VARCHAR(100)
);

-- Vitals Table
CREATE TABLE vitals (
    vital_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    blood_pressure VARCHAR(20),
    heart_rate INT,
    temperature FLOAT,
    date_recorded DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Follow-up Table
CREATE TABLE followup (
    followup_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    followup_date DATE,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Delivery Table
CREATE TABLE delivery (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    delivery_date DATE,
    delivery_method VARCHAR(20),
    complications BOOLEAN,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
