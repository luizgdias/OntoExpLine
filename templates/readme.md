# OntoExpLine
An Ontology for Experiment Lines.

## Overview

This repository presents a guide for OntoExpLine, an ontology for experiment lines, which give support to scientists to derive workflows that are composed of variant programs that implement the same activity on the flow.
Using OntoExpLine is possible to relate different kind of data and provenance, and apply reasoners mechanisms to query data used to create the scientific experiment and the data product generated during the experiment execution. OntoExpLine is composed of four specific modules: workflow structure, experiment line, domain-data branch, and metadata block.


## Introduction

Scientific experiments involve several combinations of data and abstract activities on the flow. Besides this, there are many equivalences in the workflow construct process because different concrete programs can implement an abstract activity, and these programs can consume and generate different resources. However necessary, derive workflows is an intricate work because abstract tasks, concrete programs, and their compatibilities should be defined and connected to compose the flow variations. Based on this, apply formal models can help scientists to derive the workflow in an experiment line set. This kind of model gives support to scientists to realize different kinds of verifications to confirm or refute a scientific hypothesis, applying inference  mechanisms such as reasoners.

This document presents OntoExpLine, a model for Experiment Lines that aims to give support in workflow derivation processes. The ontology is the result of the integration of different task and domain ontologies: ProveONE, Experiment Line approach proposed by Ogasawara et al., 2009, DCMI and EDAM branches.


## Aspect covered by OntoExpLine
(tipos de dados relacionados - workflow, linha de experimento, metadados, domínio, tabela de classes e propriedades)
OntoExpLine aims to provide the fundamental information required to understand and analyze scientific workflow-based on the derivable profile in their abstract activities. The structure uses domain data to create variations and metadata to explain their use in the context of experiment lines. This way, OntoExpLine is based on four ontologies: ProveONE [] to define the structure of the workflow, EDAM [] to take the domain data, Experiment Line [] to structure the derivations on the experiment line definitions, and DCMI[] to aggregate the metadata. 

## OntoExpLine Conceptual Model 
(esquema de relacionamentos das classes)
## OntoExpLine Specification
(descrição das classes - has super-class, is in domain of, is in range of - examplos de funcionamento)

## References
