from flask import Flask
import platform
import socket
import uuid



app = Flask(__name__)

@app.route('/')
def welcome():
    """docstring for welcome"""
    return "Welcome to my test application"

@app.route('/system')
def systeminfo():
    machineArch = platform.machine()
    nodeName = platform.node()
    osCheck = platform.system()
    curHost = socket.gethostbyname(socket.gethostname())

    message = "System Infomation:\nMachine:{}\nNode:{}\nOS:{}\nHost:{}".format(machineArch, nodeName, osCheck, curHost)

    return message

@app.route('/api/gentoken')
def gentoken():
    token = uuid.uuid4()
    return "You're Security ID:{}".format(token)



if __name__ == "__main__":
    app.debug = True
    app.run()
