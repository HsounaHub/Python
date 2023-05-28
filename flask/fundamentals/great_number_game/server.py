from flask import Flask, render_template, session, redirect, request
import random

app= Flask (__name__)
app.secret_key="tetststgdkfij"
@app.route('/')
def index():
    if "answer" not in session :
        session["answer"]=random.randint(1,101)
    return render_template("index.html")
@app.route('/guess',methods=["POST"])
def play():
    session['guess']=int(request.form["num"])
    return redirect('/')

@app.route('/replay')
def replay_ninja():
    session.clear()
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)