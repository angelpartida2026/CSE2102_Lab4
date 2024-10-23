from flask import Flask, request

app = Flask(__name__)

users = {
    "angel.partida@uconn.edu": "f99aa8b8573062e9802f4fc0807ae1cb"
}

@app.route("/")
def hello():
   return "You called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route("/login", methods=['POST'])
def login():
   auth_data = request.form
   user_id = auth_data.get('id')
   token = auth_data.get('token')
   if users.get(user_id) == token:
      return "Login successful", 200
   else:
      return "Invalid credentials", 401 

if __name__ == "__main__":
   app.run(host='0.0.0.0')