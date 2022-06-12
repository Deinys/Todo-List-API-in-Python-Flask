from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [{"label":"my first task for today", "done":False}, {"label": "go for dinner", "done":False}]

@app.route("/todos",methods=["GET"])
def handle_todos():
    return  jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    new_todo = {"label":"Take the dog for walk", "done":False}
    todos.append(new_todo)
    return jsonify(todos)

@app.route("/todos/<int:position>", methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete ", position)
    todos.pop(position)
    return jsonify(todos)



if __name__=="__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)