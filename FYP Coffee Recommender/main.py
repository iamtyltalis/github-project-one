# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:46:02 2021

@author: kitsune
"""
#FYP

import streamlit as st
import pandas as pd
import numpy as np

#retrieve dataset
df = pd.read_csv(r"cofe.csv")

#convert the columns containing attributes to numpy array, store in s_array
s_array = df[["aroma", "acidity", "body", "flavor", "with_milk"]].to_numpy()

st.title("FYP Coffee Recommender")
    
st.write(""" Choose Preferences """)

#ask user for aroma, acidity, body and flavor preferences using a slider
aroma = st.slider("Aroma", 1, 10)

acidity = st.slider("Acidity", 1, 10)

body = st.slider("Body", 1, 10)

flavor = st.slider("Flavor", 1, 10)

#ask user if they prefer wtih milk or without
milk_selection = st.selectbox("Milk selection", ("Without Milk", "With Milk"))

#define function
def milk_or_not(m):
    if milk_selection == "Without Milk":
        m = 0
    elif milk_selection == "With Milk":
        m = 1
    return m

milk = milk_or_not(milk_selection)

#add user input as list into variable userInp
userInp = [aroma, acidity, body, flavor, milk]

#initialize array for user input called u_array and convert list to numpy array
u_array = np.array(userInp)

#variable similairty_scores stores all tuples containing the similarity scores
similarity_scores = s_array.dot(u_array)/ (np.linalg.norm(s_array, axis=1) * np.linalg.norm(u_array))

#get the maximum element from a Numpy array
maxElement = np.amax(similarity_scores)

#find the index of the tuple with the highest similarity
indexOfMostSim = np.where(similarity_scores == np.amax(similarity_scores))

#store the index in variable index, it can be used later to find the item in the pandas dataframe.
index = indexOfMostSim[0][0]

#similarity coffee example in dataframe
#display data in the dataframe
cf = df.loc[index]
cf[["bean_brand", "aroma", "acidity", "body", "flavor", "with_milk"]]

#pulling data from dataframe into its own variables
number_str = cf.at['bean_brand']
beanb = str(number_str)
print("Bean Brand: ", beanb)

number_str = cf.at['aroma']
aroma = int(number_str)
print("Aroma: ", aroma)

number_str = cf.at['acidity']
acidity = int(number_str)
print("Acidity: ", acidity)

number_str = cf.at['body']
body = int(number_str)
print("Body: ", body)
      
number_str = cf.at['flavor']
flavor = int(number_str)
print("Flavor: ", flavor)

number_str = cf.at['with_milk']
milk = int(number_str)
print("with_milk: ", milk)
