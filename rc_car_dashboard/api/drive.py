from flask import Blueprint, request, jsonify

from autocar.car import AutoCar

bp = Blueprint("drive", __name__)

car = AutoCar()


@bp.route("/api/drive", methods=["POST"])
def drive():

    data = request.get_json()

    command = data["command"]

    if command == "forward":
        car.forward()

    elif command == "backward":
        car.backward()

    elif command == "left":
        car.left()

    elif command == "right":
        car.right()

    elif command == "stop":
        car.stop()

    return jsonify(
        {
            "success": True
        }
    )


@bp.route("/api/speed", methods=["POST"])
def speed():

    data = request.get_json()

    car.set_speed(data["speed"])

    return jsonify(
        {
            "success": True
        }
    )