#! /usr/bin/python2.7

# -*- coding:utf-8 -*-
from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def accueil():
    mots = ["bonjour", "a", "toi,", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)


@app.route('/contact/')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)
    #print app.root_path
