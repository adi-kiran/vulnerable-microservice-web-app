from flask import Flask, render_template,jsonify,request,abort
# import requests
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods=["GET"])
def test():
    return "Hello World",200

@app.route("/api/ping",methods=["POST"])
def list_add_user():
    # with open("abc.txt","w") as f:
    #     print("hello",file=f)
    if request.method == 'POST':
        # with open("abc.txt","a") as f:
        #     print("hello1",file=f)
        IP = request.get_json()["IP"]
        # with open("abc.txt","w") as f:
        #     print("hello2",file=f)
        #     print(IP,file=f)
        #     print("hello3",file=f)
        cmd = "ping -c 4 "+IP
        stream = os.popen(cmd)
        output = stream.read()
        return output,200
    else:
        return 405

if __name__ == '__main__':
    app.debug = True
    app.run(port=8080,host='0.0.0.0')
