from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')          
def hello_world():
    return 'Hello World!'  
@app.route('/play/<int:tim>/<colr>')
def play(tim,colr):
    return render_template("play.html",times=tim,colr=colr)




if __name__=="__main__":
    app.run(debug=True)

