#! /usr/bin/python3.4

# -*- coding:utf-8 -*-
from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def accueil():
    mots = ["bonjour", "a", "toi,", "visiteur."]
    return render_template('index.html', titre="Bienvenue !", mots=mots)


@app.route('/contact1/')
def contact1():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Vous avez envoye : {msg}".format(msg=request.form['msg'])
    return '<form action="" method="post"><input type="text" name="msg" /><input type="submit" value="Envoyer" /></form>'

if __name__ == '__main__':
    app.run(debug=True)
    #print app.root_path
