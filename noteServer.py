from flask import Flask, request,send_from_directory
import socket

app = Flask(__name__)

@app.route("/Note/<userName>",methods=["GET"])
def get_index(userName):
    # print("name is "+ userName)
    response = ""
    with open("index.htm","r",encoding="utf-8") as f:
        response += f.read()
    if response == "":
        return response
    note = ""
    try:
        with open("../note/"+userName+".md","r",encoding="utf-8") as n:
            note += n.read()
    except FileNotFoundError as e:
        return response
    return response.replace("<textarea id=\"text-box\" Spellcheck=\"false\"></textarea>","<textarea id=\"text-box\" Spellcheck=\"false\">"+note+"</textarea>")

@app.route("/Note/res/<fileName>",methods=["GET"])
def get_res(fileName):
    filePath = "res/"+ fileName
    try:
        with open(filePath,"r",encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        return e

@app.route("/Note/<userName>",methods=["POST"])
def save_to_file(userName):
    # print("-------------------------------------------")
    # print(request.form.get(key="text",type=str,default=None))
    # print("-------------------------------------------")
    with open("../note/"+userName+".md","w+",encoding="utf-8") as f:
        f.write(request.form.get(key="text",type=str,default=None))
    return "OK",200

@app.route('/favicon.ico')#设置icon
def favicon():
    return send_from_directory(".",#对于当前文件所在路径,比如这里是static下的favicon.ico
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/bower_components/showdown/dist/<path:filename>",methods=["GET"])
def get_bower_components(filename):
    filePath = "bower_components/showdown/dist/"+filename
    try:
        with open(filePath,"r",encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        return e

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def save_to_file(userName):
    # print("-------------------------------------------")
    # print(request.form.get(key="text",type=str,default=None))
    # print("-------------------------------------------")
    with open("note/"+userName+".md","w+",encoding="utf-8") as f:
        f.write(request.form.get(key="text",type=str,default=None))
    return "OK",200
if __name__ == "__main__":
    print("Server Address:"+extract_ip()+":8080/Note/'your name'")
    app.run(host=extract_ip(),port="8080")
