from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!'  
@app.route('/dojo')          
def dojo():
    return 'Dojo!'  
@app.route('/say/<string:name>')          
def say_my_name(name):
    return f"Hi {name}!"  
@app.route('/repeat/<int:numb>/<string:name>')          
def repeat(name,numb):
    return f"<h1>{name}</h1>"*numb
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."






if __name__=="__main__":   
    app.run(debug=True)    