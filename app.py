#! /usr/bin/python3.4

# -*- coding:utf-8 -*-
from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
@app.route('/running_wc/')
def running_wc():
    running_working_copies = ["wc1", "wc2"]
    wc_projects = ["Irma", "Axtdocprocess", "idocdb"]
    return render_template('running_wc.html', title="OcrCI", working_copies=running_working_copies, projects=wc_projects)


@app.route('/working_copies/')
def working_copies():
    return render_template('working_copies.html', title="OcrCI")


@app.route('/aptly/')
def aptly():
    return render_template('aptly.html', title="OcrCI")


@app.route('/system/')
def system():
    return render_template('system.html', title="OcrCI")


@app.route('/debian_tools/')
def debian_tools():
    return render_template('debian_tools.html', title="OcrCI")


if __name__ == '__main__':
    app.run(debug=True)
    #print app.root_path
