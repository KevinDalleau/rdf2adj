# rdf2adj

## Introduction

This Python module provides a way to transform an RDF graph in an adjacency list (only for specific nodes).

## Installation

Within the root of the repository.
    pip install .

## Usage

    import rdf2adj
    adj = rdf2adj.RdfGraph()

To fit the RdfGraph object to an RDF file, use the .fit(path, format, individualSpecifier). For example :  

    adj.fit("./example_file.n3","n3","<http://swrc.ontoware.org/ontology#affiliation>")

fits the graph with the data contained in example_file, written following the n3 specs, and where the individuals nodes to keep are specified with a specific relation.

Once the RdfGraph() object fitted, it is then possible to retrieve : 

    adj.graph_adj : the adjacency list
    adj.individuals : a list of the individuals
    adj.y : the classes for each of the individuals
