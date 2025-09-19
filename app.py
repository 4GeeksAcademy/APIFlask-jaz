from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista inicial de tareas (todos)
todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": True}
]

# GET /todos -> devuelve la lista de tareas
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200


# POST /todos -> agrega una nueva tarea
@app.route("/todos", methods=["POST"])
def add_todo():
   
    new_todo = request.get_json()
    if not new_todo or "label" not in new_todo or "done" not in new_todo:
        return jsonify({"error": "El body debe contener 'label' y 'done'"}), 400

    todos.append(new_todo)
    return jsonify(todos), 201


# DELETE ,elimina una tarea por posición
@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición fuera de rango"}), 404

    todos.pop(position)
    return jsonify(todos), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
