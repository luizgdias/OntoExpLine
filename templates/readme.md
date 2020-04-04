# OntoExpLine
An Ontology for Experiment Lines.

## Overview

This repository presents a guide for OntoExpLine, an ontology for experiment lines, which give support to scientists to derive workflows that are composed of variant programs that implement the same activity on the flow.
Using OntoExpLine is possible to relate different kind of data and provenance, and apply reasoners mechanisms to query data used to create the scientific experiment and the data product generated during the experiment execution. OntoExpLine is composed of four specific modules: workflow structure, experiment line, domain-data branch, and metadata block.


## Introduction

Scientific experiments involve several combinations of data and abstract activities on the flow. Besides this, there are a lot of equivalences in the concrete workflow implementation process because an abstract activity can be implemented by different concrete programs, and these programs can consume and generate different datasets. In addition, the systems that perform workflows do not associate variations of these activities as the knowledge used to create the variations are often not explicit and comes from specialists involved in the development of the experiment.

## Aspect covered by OntoExpLine
(tipos de dados relacionados - workflow, linha de experimento, metadados, domínio, tabela de classes e propriedades)
OntoExpLine aims to provide the fundamental information required to understand and analyze scientific workflow-based on the derivable profile in their abstract activities. The structure uses domain data to create variations and metadata to explain their use in the context of experiment lines. This way, OntoExpLine is based on four ontologies: ProveONE [] to define the structure of the workflow, EDAM [] to take the domain data, Experiment Line [] to structure the derivations on the experiment line definitions, and DCMI[] to aggregate the metadata. 

## OntoExpLine Conceptual Model 
(esquema de relacionamentos das classes)
## OntoExpLine Specification
(descrição das classes - has super-class, is in domain of, is in range of - examplos de funcionamento)

## References
