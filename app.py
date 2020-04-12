from flask import Flask, redirect, url_for, render_template
from owlready2 import *
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from individualDTO import Individual

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

@app.route("/derivations.html")
def derivations():
    return render_template("derivations.html")

def ontologyStructure():
    onto = get_ontology("ontoexpline.owl")
    onto.load() 

    # imprimindo instancias de uma classe
    # for i in onto.ProvOne.instances(): print(i)
    # print(onto.ProvOneData.is_a)


    ontoexpline = [[],[],[],[]]
    # ontoexplineEntity = []

    for item in onto.classes():
        # print(item, item.is_a)
        if(((onto.ProvOne) in list(item.is_a)) or ((onto.Entity) in list(item.is_a)) or ((onto.Program) in list(item.is_a))):
            comments = ''
            for x in item.comment:
                comments = comments+x
            
            individualsList     = item.instances()
            propertiesList      = item.seeAlso
            if(len(propertiesList) == 0): propertiesList = "-"
            if(len(individualsList) == 0): individualsList = "-"
            isaList             = item.is_a
            ontoExpLineClass    = Individual(str(item).replace("ontoexpline.", ""), comments, isaList, propertiesList, individualsList)
            ontoexpline[0].append(ontoExpLineClass)
        

        if(((onto.Experiment_Line) in list(item.is_a)) or ((onto.Type) in list(item.is_a)) or ((onto.Activity_Type) in list(item.is_a))):
            comments = ''
            for x in item.comment:
                comments = comments+x

            individualsList     = item.instances()
            propertiesList      = item.seeAlso
            isaList             = item.is_a

            if(len(propertiesList) == 0): propertiesList = "-"
            if(len(individualsList) == 0): individualsList = "-"

            ontoExpLineClass = Individual(str(item).replace("ontoexpline.", ""), comments, isaList, propertiesList, individualsList)
            ontoexpline[1].append(ontoExpLineClass)

        if(((onto.Program_Type) in list(item.is_a))):
            comments = ''
            for x in item.comment:
                comments = comments+x
            
            individualsList     = item.instances()
            propertiesList      = item.seeAlso
            isaList             = item.is_a

            if(len(propertiesList) == 0): propertiesList = "-"
            if(len(individualsList) == 0): individualsList = "-"

            ontoExpLineClass = Individual(str(item).replace("ontoexpline.", ""), comments, isaList, propertiesList, individualsList)
            ontoexpline[2].append(ontoExpLineClass)

        
        if(((onto.Metadata) in list(item.is_a))):
            comments = ''
            for x in item.comment:
                comments = comments+x
            
            individualsList     = item.instances()
            propertiesList      = item.seeAlso
            isaList             = item.is_a

            if(len(propertiesList) == 0): propertiesList = "-"
            if(len(individualsList) == 0): individualsList = "-"

            ontoExpLineClass = Individual(str(item).replace("ontoexpline.", ""), comments, isaList, propertiesList, individualsList)
            ontoexpline[3].append(ontoExpLineClass)

    return ontoexpline
# verifica se o user está executando o arquivo principal
if __name__ == "__main__":
    app.run(debug=True)