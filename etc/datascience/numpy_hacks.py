#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:49:52 2018

@author: balint
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier




def score_succession(ground_truth, predictions, categories):
    categories = np.array(categories)
    ground_truth = np.array(ground_truth)

    choice_index = []
    for t in ground_truth:
        choice_index.append(t == categories)

    choice_index = np.stack(choice_index)
    actual_confidence = predictions[choice_index]
    succession = np.sort(predictions)

    score = 0
    for confs, actual in zip(succession, actual_confidence):
        score += np.where( np.flip(np.sort(confs), axis=0) == actual)[0][0]

    return score / ground_truth.shape[0]




if __name__ == "__main__":
    
 
    clf = RandomForestClassifier(random_state=10)

    x,y = make_classification(n_features=10, n_classes=3, n_informative=3)

    clf.fit(x,y)

    preds = clf.predict_proba(x)  # lol

    print(preds)

    print(y)

    print(score_succession(y, preds, [0,1,2]))




