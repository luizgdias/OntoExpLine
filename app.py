from flask import Flask, redirect, url_for, render_template
from owlready2 import *
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from individualDTO import Individual
from abstractActivityDTO import AbstractActivity

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
    onto = get_ontology("ontoexpline.owl")
    onto.load() 

    result = onto.get_instances_of(onto.Abstract_activity)
    programsInstances = onto.get_instances_of(onto.Program)
    result_replaced = []
    objectList = []
    programList = []
    # print(programsInstances)
    for i in result:
        abstractActivityDTO = AbstractActivity('', '', '', '', '')
        abstractActivityDTO.setName(i)
        if(onto.Variant in i.is_a):
            abstractActivityDTO.setActivityType(onto.Variant)
        if(onto.Mandatory in i.is_a):
            abstractActivityDTO.setActivityType(onto.Mandatory)
        if(onto.Optionaly in i.is_a):
            abstractActivityDTO.setActivityType(onto.Mandatory)
        abstractActivityDTO.setInputRelations(i.hasInputRelation)
        abstractActivityDTO.setOutputRelations(i.hasOutputRelation)
        for program in programsInstances:
            if (i in program.implements):
                programList.append(program)
            abstractActivityDTO.setImplementedBy(programList)
        programList = []
            # print(str(program)+' implements: ' + str(program.implements))

            
        # x = (onto.search(is_a = onto.Abstract_activity, hasInputRelation = onto.search_one(label = "r1")))

        objectList.append(abstractActivityDTO)
        i = str(i).replace("ontoexpline.","")
        result_replaced.append(i)

    return render_template("derivations.html", result = result_replaced, objectList = objectList)

def ontologyStructure():
    onto = get_ontology("ontoexpline.owl")
    onto.load() 

    ontoexpline = [[],[],[],[]]

    for item in onto.classes():
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