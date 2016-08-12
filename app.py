#! /usr/bin/python3.4

# -*- coding:utf-8 -*-
from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
@app.route('/running_wc/')
def running_wc():
    working_copies = ["wc1", "wc2"]
    projects = ["Irma", "Axtdocprocess", "idocdb"]
    return render_template('running_wc.html', title="OcrCI", working_copies=working_copies, projects=projects)


@app.route('/working_copies/')
def working_copies():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


@app.route('/aptly/', methods=['GET', 'POST'])
def aptly():
    if request.method == 'POST':
        return "Vous avez envoye : {msg}".format(msg=request.form['msg'])
    return '<form action="" method="post"><input type="text" name="msg" /><input type="submit" value="Envoyer" /></form>'


@app.route('/system/')
def system():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


@app.route('/debian_tools/')
def debian_tools():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)
    #print app.root_path
