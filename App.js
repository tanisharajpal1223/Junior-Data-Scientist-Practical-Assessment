import React, { useState, useEffect } from 'react';

const App = () => {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/patients')
      .then(response => response.json())
      .then(data => setPatients(data));
  }, []);

  return (
    <div className="App">
      <h1>Patient Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>Patient ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Gender</th>
          </tr>
        </thead>
        <tbody>
          {patients.map((patient) => (
            <tr key={patient.id}>
              <td>{patient.id}</td>
              <td>{patient.first_name}</td>
              <td>{patient.last_name}</td>
              <td>{patient.gender}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
