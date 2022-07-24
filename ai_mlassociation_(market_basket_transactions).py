# -*- coding: utf-8 -*-
"""AI: MLAssociation (Market Basket Transactions).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ERSCjvUQfhuiqJTvPn2QwrTkG8-b02wZ
"""

# Imports
# Link 1: https://www.geeksforgeeks.org/apriori-algorithm/?ref=lbp
# Link 2: https://www.geeksforgeeks.org/apriori-algorithm/?ref=lbp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
!pip install apyori
from apyori import apriori

# Data
# Dataset: https://www.kaggle.com/datasets/irfanasrullah/groceries
dataFile = "//content//drive//MyDrive//Coding//Personal Projects//1: Artificial Intelligence//Resources//MarketBasketTransactions.csv"
data = pd.read_csv(dataFile)
data = data.values.tolist()
allTransactions = []
for row in data:
  singleTransaction = []
  for item in range(1, len(row)): # row 1 is not needed
    if str(row[item]) == "nan":
      break
    else:
      singleTransaction.append(row[item])
  allTransactions.append(singleTransaction)

# Apiori Algorithm

associationRules = apriori(allTransactions, min_support = 0.002, min_confidence = 0.5, min_length = 2)
ruleList = list(associationRules)
ruleList = pd.DataFrame(ruleList)
ruleListSample = ruleList.head(10)
print(ruleListSample)