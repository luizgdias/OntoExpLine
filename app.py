from flask import Flask, redirect, url_for, render_template
from owlready2 import *
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from individualDTO import Individual
from abstractActivityDTO import AbstractActivity
from variationsDTO import Variation

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

def traceVariation(item, onto, variation):
    x = onto.get_instances_of(onto.Program)
    itemPort = item.hasOutPort

    for portas in itemPort:
        itemChannel = portas.connectsTo
    
    for i in x:
        iPort = i.hasOutPort
        for iPortas in iPort:
            iChannel = iPortas.connectsTo

        if (( i != item) and (itemChannel == iChannel)):
            print(str(item)+" / "+ str(i) + " usam o mesmo canal")
            variation.append(item)
    return variation
    
@app.route("/derivations.html")
def derivations():
    onto = get_ontology("ontoexpline.owl")
    onto.load() 

    result = onto.get_instances_of(onto.Abstract_activity)
    programsInstances = onto.get_instances_of(onto.Program)
    result_replaced = []
    objectList = []
    programList = []

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
        objectList.append(abstractActivityDTO)
        # i = str(i).replace("ontoexpline.","")
        result_replaced.append(i)
    # print(result_replaced)

    line = []
    fonte = []
    sumidouro = []
    # Verifica a consistencia do relacionamento das abstract activities e monta o fluxo
    # Fonte e a cabeça do flow, e sumidouro é a ultima atividade do flow
    for i in objectList:
        if(i.getInputRelations() == []):
            fonte = i #encontrou a primeira atividade do flow
        if(i.getOutputRelations() == []):
            sumidouro = i #encontrou a ultima atividade do flow
    
    line.append(fonte)
    #encontrando as atividades intermediárias entre a fonte e o sumidouro (comparando as relações de i/o):
    for i_a2 in objectList:
        if i_a2.getInputRelations() == fonte.getOutputRelations():
            line.append(i_a2)
            for i_a3 in objectList:
                if i_a3.getInputRelations() == i_a2.getOutputRelations():
                    line.append(i_a3)
                    for i_a4 in objectList:
                        if i_a4.getInputRelations() == i_a3.getOutputRelations():
                            line.append(i_a4)
    line.append(sumidouro) 
    # line é a linha do sciphy, cabeçalho da tabela de derivações
    act1 = onto.get_instances_of(onto.Sequencing_quality_control)
    act2 = onto.get_instances_of(onto.Sequence_alignment_operation_0292)
    act3 = onto.get_instances_of(onto.Sequence_alignment_conversion)
    act4 = onto.get_instances_of(onto.Sequence_alignment_refinament)
    act5 = onto.get_instances_of(onto.Phylogenetic_tree_generation)
    
    derivation = []
    indice = []
    i = 1
    derivations = []
    #para cada programa que implementa uma atividade, pegar o programa
    for program_act1 in act1:
        for program_act2 in act2:
            for program_act3 in act3:
                for program_act4 in act4:
                    for program_act5 in act5:
                        # após pegar o programa, pegar a porta do programa
                        for port_out_act1 in program_act1.hasOutPort:
                            for port_in_act2 in program_act2.hasInPort:
                                    # após pegar as portas dos programas, verificar se elas se conectam no mesmo channel, se sim, append na derivação
                                    if((port_out_act1.connectsTo == port_in_act2.connectsTo)):
                                        derivation.append(program_act1)
                                        derivation.append(program_act2)
                                    
                                    for port_out_act2 in program_act2.hasOutPort: 
                                        for port_in_act3 in program_act3.hasInPort:
                                        
                                            if((port_out_act2.connectsTo == port_in_act3.connectsTo)):
                                                derivation.append(program_act3)
                                            
                                            for port_out_act3 in program_act3.hasOutPort: 
                                                for port_in_act4 in program_act4.hasInPort:

                                                    if((port_in_act4.connectsTo == port_out_act3.connectsTo)):
                                                        derivation.append(program_act4)

                                                    for port_out_act4 in program_act4.hasOutPort: 
                                                        for port_in_act5 in program_act5.hasInPort:

                                                            if((port_out_act4.connectsTo == port_in_act5.connectsTo)):
                                                                derivation.append(program_act5)
                                                                derivation.insert(0, i)
                                                    i = i+1
                                                    derivations.append(derivation)
                                                    indice.append(i)
                                                    derivation = []
                                                # print(program_act2, port_act2, port_act2.connectsTo, port_act3.connectsTo, port_act3, program_act3)
    print(derivations)
                

    return render_template("derivations.html", result = result_replaced, objectList = line, derivations = derivations, indice = indice)

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