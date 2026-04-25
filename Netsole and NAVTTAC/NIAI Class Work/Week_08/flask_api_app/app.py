from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database (list)
students = []

# Home route
@app.route('/')
def home():
    return "Student API is running!"

# Add student (POST)
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json

    student = {
        "id": len(students) + 1,
        "name": data.get("name"),
        "age": data.get("age"),
        "course": data.get("course")
    }

    students.append(student)

    return jsonify({
        "message": "Student added successfully",
        "student": student
    })

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Get single student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)