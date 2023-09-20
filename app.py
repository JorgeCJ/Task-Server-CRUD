from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET'])
def index():
    return 'Server is running'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {"id" : len(tasks) + 1 , "task": data["task"]}
    tasks.append(new_task)
    return jsonify(new_task), 201
    
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = data["task"]
            return jsonify(task)
    return jsonify({"error":"Task not found"})

@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug = True)