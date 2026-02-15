from flask import Blueprint, request, jsonify
import uuid

tasks_bp = Blueprint("tasks", __name__)

# Temporary in-memory storage
TASKS = {}


@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json() or {}

    task_id = str(uuid.uuid4())

    task = {
        "id": task_id,
        "name": data.get("name", "default-task"),
        "status": "created"
    }

    TASKS[task_id] = task

    return jsonify(task), 201


@tasks_bp.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    task = TASKS.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@tasks_bp.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(list(TASKS.values())), 200