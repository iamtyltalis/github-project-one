# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:46:02 2021

@author: kitsune
"""
#FYP

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from googlesearch import search 

#import image
image  = Image.open(r"image.png") 
st.image(image, width=None)

#retrieve dataset
df = pd.read_csv(r"cofe.csv")

#convert the columns containing attributes to numpy array, store in s_array
s_array = df[["aroma", "acidity", "body", "flavor", "with_milk"]].to_numpy()

st.title("FYP Coffee Recommender")

st.markdown('**This app recommends coffee bean brands to you. All you need to do is to input \
            your preferred coffee attributes and the let the system do the rest!**')


#ask user if they prefer wtih milk or without
milk_selection = st.selectbox("Milk selection", ("Without Milk", "With Milk"))

#define function for milk or no milk
def milk_or_not(m):
    if milk_selection == "Without Milk":
        m = 0
    elif milk_selection == "With Milk":
        m = 1
    return m

milk = milk_or_not(milk_selection)

#ask user for aroma, acidity, body and flavor preferences using a slider
aroma = st.slider("Aroma", 1, 10)

acidity = st.slider("Acidity", 1, 10)

body = st.slider("Body", 1, 10)

flavor = st.slider("Flavor", 1, 10)

#add user input as list into variable userInp
userInp = [aroma, acidity, body, flavor, milk]

#initialize array for user input called u_array and convert list to numpy array
u_array = np.array(userInp)

#variable similairty_scores stores all tuples containing the similarity scores
similarity_scores = s_array.dot(u_array)/ (np.linalg.norm(s_array, axis=1) * np.linalg.norm(u_array))

#find the index of the tuple with the highest similarity
indexOfMostSim = np.where(similarity_scores == np.amax(similarity_scores))

#store the index in variable index, it can be used later to find the item in the pandas dataframe.
index = indexOfMostSim[0][0]

#similarity coffee example in dataframe
#display data in the dataframe
cf = df.loc[index]

##cf[["bean_brand", "aroma", "acidity", "body", "flavor", "with_milk"]]

#Looks for the region in dataframe
reg = "Unknown"
if cf.at['region_africa_arabia'] == 1:
    reg = "Africa Arabia"
elif cf.at['region_caribbean'] == 1:
    reg = "Caribbean"
elif cf.at['region_central_america'] == 1:
    reg = "Central America"
elif cf.at['region_hawaii'] == 1:
    reg = "Hawaii"
elif cf.at['region_asia_pacific'] == 1:
    reg = "Asia Pacific"
elif cf.at['region_south_america'] == 1:
    reg = "South America"

#prints results
def print_results():
    
    st.markdown('**Your Recommended Coffee is: ** :coffee:')
            
    #pulling data from dataframe into its own variables
    number_str = cf.at['bean_brand']
    global beanb
    beanb = str(number_str).replace('-', ' ').upper()
    st.text("Bean Brand: " + beanb)
    
    number_str = cf.at['aroma']
    aroma = int(number_str)
    st.text("Aroma: " + str(aroma))
    
    number_str = cf.at['acidity']
    acidity = int(number_str)
    st.text("Acidity: " + str(acidity))
    
    number_str = cf.at['body']
    body = int(number_str)
    st.text("Body: " + str(body))
          
    number_str = cf.at['flavor']
    flavor = int(number_str)
    st.text("Flavor: " + str(flavor))
    
    number_str = cf.at['with_milk']
    milk = int(number_str)
    st.text("With milk: " + str(milk))
    
    st.text("Region: " + str(reg))

print_results()

st.markdown('**More information can be found in the links provided:** :coffee:')
#streamlit button. when pressed, it prints links of the top 5 google search results after 1.5 seconds.
if st.button('Search Google'):
    #beanb = the name of the bean to search, number = results to display
    count = 0
    for j in search(beanb, tld="co.in", num=5, stop=5, pause=1.5): 
        count = count + 1
        st.write(count, j)
