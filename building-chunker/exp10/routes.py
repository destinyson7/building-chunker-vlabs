from flask import render_template, url_for, request, jsonify
from exp10 import app, db
from exp10.models import answersData


@app.route("/")
@app.route("/Introduction.html")
def Introduction():
    return render_template("Introduction.html")


@app.route("/Theory.html")
def Theory():
    return render_template("Theory.html")


@app.route("/Objective.html")
def Objective():
    return render_template("Objective.html")


@app.route("/Experiment.html")
def Experiment():
    db.create_all()
    data = answersData.query.all()

    s = ''

    for i in data:
        s += i.answers

    return render_template('Experiment.html', strf=s)


@app.route("/addAnswer", methods=["POST"])
def anserAdd():
    given_answer = request.form['answer']
    db.create_all()
    add_answer = answersData(given_answer)
    db.session.add(add_answer)
    db.session.commit()
    temp = {}
    temp['status'] = (type(add_answer) == answersData)
    return jsonify(temp)


@app.route("/Quizzes.html")
def Quizzes():
    return render_template("Quizzes.html")


@app.route("/Procedure.html")
def Procedure():
    return render_template("Procedure.html")


@app.route("/Further Readings.html")
def Further_Readings():
    return render_template("Further Readings.html")
