#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/coucou')
def dire_coucou():
    return 'Coucou !'

@app.route('/')
def accueil():
    return "<h1>Bienvenue !</h1>"


@app.route('/la')
def ici():
    return "Le chemin de 'ici' est : " + request.path


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return "Ma jolie page {}".format(error.code), error.code


@app.route('/google')
def redirection_google():
    return redirect('http://www.google.fr')


if __name__ == '__main__':
    app.run(debug=True)

