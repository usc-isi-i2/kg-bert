#!/usr/bin/env python3

import os,pickle
from collections import defaultdict
from pslpython.model import Model
from pslpython.partition import Partition
from pslpython.predicate import Predicate
from pslpython.rule import Rule
import pandas as pd
import time

RICA_file="./RICA/RICA_material_KnowledgeTable.csv"
MODEL_NAME = 'material_knowledge'
DATA_DIR = os.path.join('.', 'RICA', MODEL_NAME)
ADDITIONAL_PSL_OPTIONS = {
    #'log4j.threshold': 'DEBUG, A1'
}

ADDITIONAL_CLI_OPTIONS = [
    # '--postgres'
]

with open('rel.pickle', 'rb') as handle:
    rels = pickle.load(handle)
    
with open('rules.pickle', 'rb') as handle:
    rules = pickle.load(handle)
    
def main():
    model = Model(MODEL_NAME)

    # Add Predicates
    add_predicates(model)

    # Add Rules
    add_rules(model)

    # Inference
    results = infer(model)

    write_results(results, model)

def write_results(results, model):
    out_dir = 'inferred-predicates'
    os.makedirs(out_dir, exist_ok = True)

    for predicate in model.get_predicates().values():
        if (predicate.closed()):
            continue

        out_path = os.path.join(out_dir, "%s.txt" % (predicate.name()))
        results[predicate].to_csv(out_path, sep = "\t", header = False, index = False)

def add_predicates(model):
    predicate = Predicate('Material', closed = True, size = 2)
    model.add_predicate(predicate)
    
    for rel in rels:
        predicate = Predicate(rel, closed = True, size = 2)
        model.add_predicate(predicate)


    predicate = Predicate('More', closed = False, size = 3)
    model.add_predicate(predicate)
def add_rules(model):
    
    for rule in rules:
        model.add_rule(Rule(rule))

    # Negative prior.
    #model.add_rule(Rule("1: !More(I1, I2, T) ^2"))

def add_data(model):
    for predicate in model.get_predicates().values():
        predicate.clear_data()
        
    path = os.path.join(DATA_DIR, 'ItemMaterial_obs.txt')
    model.get_predicate('Material').add_data_file(Partition.OBSERVATIONS, path)
    
    for rel in rels:
        path = os.path.join(DATA_DIR, rel+'_obs.txt')
        model.get_predicate(rel).add_data_file(Partition.OBSERVATIONS, path)
    
    path = os.path.join(DATA_DIR, 'more_targets.txt')
    model.get_predicate('More').add_data_file(Partition.TARGETS, path)

    path = os.path.join(DATA_DIR, 'more_truth.txt')
    model.get_predicate('More').add_data_file(Partition.TRUTH, path)

def infer(model):
    add_data(model)
    return model.infer(additional_cli_optons = ADDITIONAL_CLI_OPTIONS, psl_config = ADDITIONAL_PSL_OPTIONS)

if (__name__ == '__main__'):
    main()