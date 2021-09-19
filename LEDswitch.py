from flask import Flask, jsonify, request, make_response, abort
from flask_cors import CORS, cross_origin
from gpiozero import LED
import time


light = {"status": "good"}
led =LED(18)


@app.route('/switch', methods=['PUT'])
@cross_origin(origin="*")
def switcher():
    boy2 = request.json['status']
    light[0]['status'] = boy2
    status(boy2)
    return "status recieved"


def status(lighting):
  if lighting == "on":
      print("LED On")
      led.on()
  elif lighting == "off":
      print("LED off")
      led.off()


@app.route('/switch', methods=['GET'])
@cross_origin(origin="*")
def switch():
    return jsonify(light)


if __name__ == '__main__':
    app.run()
