import os

import numpy as np
import pandas as pd

# Read train data from "./data/train.csv"
# Clean data
# Get a model from training
# Use the model to determine test data "./data/test.csv"
# Output the result to "./submission/"

#Model 1
#  Just for test, compute all distrubution data relation
#  (which means case A with higher to die)

ROOT_PATH = os.path.dirname(os.path.abspath( __file__ ))
train_data = pd.read_csv(ROOT_PATH + "/data/train.csv")
test_data = pd.read_csv(ROOT_PATH + "/data/test.csv")



#results = pd.DataFrame({
#        'PassengerId' : test_data['PassengerId'],
#        'Survived' : predict_num
#    })

#results.to_csv(ROOT_PATH + "/submission/submission.csv", index=False)
