import time
from flask import Flask,jsonify,request,make_response,abort
from flask_cors import CORS, cross_origin
import pyodbc
import json
#import RPi.GPIO as GPIO
#import time

conn = pyodbc.connect("DRIVER={SQL Server}; Server=.\SQLEXPRESS; Database=PersonalBio/Home; Trusted_Connection=yes;")

cursor = conn.cursor()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

task = [{

        "hi": "you",
        "go": "do"
}]

light = [{
        "status": "good"
        }]


@app.route('/', methods=['GET'])
@cross_origin(origin="*")
def api():
    cursor.execute("SELECT classTitle, name, Img FROM Home")
    s = cursor.fetchall()
    g = []
    for row in cursor.description: 
        g.append(row[0])
    a = {}
    h=[]
    for rows in s:
        for i in range(0,len(rows)):
            a[g[i]] = rows[i]
        h.append(a)
        a={}
    #d = json.dumps(s)
    #a = json.loads(d)
    #  cursor.close()
    #return jsonify(s)
    #return jsonify(task)
    return jsonify(h)

@app.route('/table', methods=['GET'])
@cross_origin(origin="*")
def tableInfo():
    return 'tables'

@app.route('/table', methods=['POST'])
@cross_origin(origin="*")
def tableAdd():
    title = request.json['table']
    cursor.execute(f"CREATE TABLE {title} (names text)")
    conn.commit()
    return jsonify({'status': 'add'})


@app.route('/table', methods=['DELETE'])
@cross_origin(origin="*")
def tableDelete():
    title = request.json['table']
    cursor.execute(f"DROP TABLE {title}")
    conn.commit()
    return jsonify({'status': 'deleted'})


@app.route('/form', methods=['GET'])
@cross_origin(origin="*")
def FormInfo():
    return 'forms'

@app.route('/form', methods=['POST'])
@cross_origin(origin="*")
def formAdd():
    title = request.json
    cursor.execute("INSERT INTO {} VALUES (\'{}\',\'{}\',\'{}\')".format(title['UsedTable'],
    title['name'], title['password'], title['date']))
    conn.commit()
    return jsonify({'status': 'Row_add'})


@app.route('/form', methods=['DELETE'])
@cross_origin(origin="*")
def formDelete():
    title = request.json
    cursor.execute("DELETE FROM {} WHERE 'name' = {}".format(
        title['UsedTable'], title['name']))
    conn.commit()
    return jsonify({'status': 'Row_deleted'})


@app.route('/project', methods=['GET'])
@cross_origin(origin="*")
def project():
    cursor.execute("SELECT classTitle, name, Img FROM Home")
    s = cursor.fetchall()
    g = []
    for row in cursor.description:
        g.append(row[0])
    a = {}
    h = []
    for rows in s:
        for i in range(0, len(rows)):
            a[g[i]] = rows[i]
        h.append(a)
        a = {}
    return jsonify(h)










@app.route('/a', methods=['PUT'])
@cross_origin(origin="*")
#supports_credentials=True)
def api2():
    boy2 = request.json['hi']
    task[0]['hi'] = boy2
    return "nice:)"

@app.route('/a', methods=['GET'])
@cross_origin(origin="*")
def projectq():

    return jsonify(task)


@app.route('/a', methods=['POST'])
@cross_origin(origin="*")
def api1():
    boy1 = request.json['do']
    print(request.json)
    task.append({'yo': boy1})
    return jsonify(task)


@app.route('/a', methods=['DELETE'])
@cross_origin(origin="*")
#supports_credentials=True)
def api3():
    boy2 = request.json['hi']
    print(type(boy2))

    task[0].pop('hi')
    return jsonify(task)




'''
api()
#robotic arm
@app.route('/', methods=['POST'])
@cross_origin(origin="*")
def api1():
    boy1 = request.json['do']
    print(request.json)
    task.append({'yo': boy1})
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    if boy1 == 'on':
        print("LED On")
        GPIO.output(pin, GPIO.HIGH)

        time.sleep(5)
        print("LED off")

        GPIO.output(pin, GPIO.LOW)
        
    GPIO.cleanup()

    return jsonify(task)

@app.route('/', methods=['POST'])
@cross_origin(origin="*")
def api1():
    boy1 = request.json['do']
    print(request.json)
    task.append({'yo': boy1})
    return jsonify(task)

@app.route('/', methods=['PUT'])
@cross_origin(origin="*")
#supports_credentials=True)
def api2():
    boy2 = request.json['hi']
    print(type(boy2))
    #print(do)
    
    task[0]['hi'] = boy2
    return jsonify(task)

@app.route('/', methods=['DELETE'])
@cross_origin(origin="*")
#supports_credentials=True)
def api3():
    boy2 = request.json['hi']
    print(type(boy2))

    task[0].pop('hi')
    return jsonify(task)



'''
#conn.close()

if __name__ == '__main__':
    app.run()


