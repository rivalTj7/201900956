#Maching learnign Imports
from sklearn.preprocessing import PolynomialFeatures
import streamlit as st;
import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.metrics import mean_squared_error, r2_score;
#Local Imports
from Records.File import File;
import re

fil = File()

def decisionTree():
    st.header(f"Data Entry in Decision Tree")

    data =  fil.OpenFile()
    if (data is not None):


        with st.form("entry_form", clear_on_submit=True):
            clas = st.selectbox("Seleccione la columna de clasificacion: ", data.keys())
            respo = st.selectbox("Seleccione la columna de Respuesta: ", data.keys())
            submitted = st.form_submit_button("Save Data")

            st.write("Valores de Interes")
            vals = st.text_input("Separar por coma")

            if submitted:
                X = np.asarray(data[clas])
                Y = np.asarray(data[respo])
                List_Val = lambda x : [int(i) for i in re.split(",",x) if i!=""]
                arraylist = List_Val(vals)
                valInit= list(map(float,arraylist))
                
                #Decision Tree configuration
                clf = DecisionTreeClassifier().fit(X, Y)
                Treedot= export_graphviz(clf,out_file=None,filled=True,rounded=True,special_characters=True)
                st.graphviz_chart(Treedot)
                st.write("Prediccion: ")
                st.write(clf.predict([valInit]))
