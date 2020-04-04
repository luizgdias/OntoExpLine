from flask import Flask, redirect, url_for, render_template
from owlready2 import *
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", content="")

@app.route("/index.html")
def home():
    return render_template("index.html", content="")

@app.route("/tutorial.html")
def tutorial():
    return render_template("tutorial.html", content="")

@app.route("/ontoexpline.html")
def ontoexpline():
    result = ontologyStructure()
    return render_template("ontoexpline.html", content="", result= result)

@app.route("/contact.html")
def contact():
    return render_template("contact.html", content="")


def ontologyStructure():
    onto = get_ontology("ontology.owl")
    onto.load() 
    print("*****************")


    # imprimindo instancias de uma classe
    # for i in onto.ProvOne.instances(): print(i)
    print(onto.ProvOneData.is_a)
    print("*****************")

    ontoexpline = [[],[],[],[]]
    for i in list(onto.classes()):
        if "ProvOne:" in str(i):
            i_replaced =str(i).replace("ontology.", "")
            ontoexpline[0].append(i_replaced)
        if "ExpLine" in str(i):
            i_replaced =str(i).replace("ontology.", "")
            ontoexpline[1].append(i_replaced)
        if "EDAM" in str(i):
            i_replaced =str(i).replace("ontology.", "")
            ontoexpline[2].append(i_replaced)
        if "DCMI" in str(i):
            i_replaced =str(i).replace("ontology.", "")
            ontoexpline[3].append(i_replaced)
    return ontoexpline
# verifica se o user está executando o arquivo principal
if __name__ == "__main__":
    app.run(debug=True)