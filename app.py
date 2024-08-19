from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('employees.json') as f:
    employees = json.load(f)

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:empid>', methods=['GET'])
def get_employee(empid):
    employee = next((emp for emp in employees if emp["empid"] == empid), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/employees/<int:empid>', methods=['PUT'])
def update_employee(empid):
    employee = next((emp for emp in employees if emp["empid"] == empid), None)
    if employee:
        data = request.get_json()
        employee.update(data)
        return jsonify({"message": "Employee updated successfully", "employee": employee})
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/employees/<int:empid>', methods=['DELETE'])
def delete_employee(empid):
    global employees
    employee = next((emp for emp in employees if emp["empid"] == empid), None)
    if employee:
        employees = [emp for emp in employees if emp["empid"] != empid]
        return jsonify({"message": "Employee deleted successfully"})
    else:
        return jsonify({"error": "Employee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
