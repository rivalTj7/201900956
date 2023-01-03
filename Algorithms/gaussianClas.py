import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from Records.File import File
import re

fil = File()
def gaussianClas():

    st.header(f"Data Entry in Gaussian Classification")

    data =  fil.OpenFile()
    if (data is not None):
        Valx=data.columns
        Valy=data.columns
        select_valxlist = st.selectbox('Valores de Columnas de interes',Valx)
        select_valylist = st.selectbox('Valores de Columna de respuesta',Valy)

        X = np.asarray(data[select_valxlist])
        Y = np.asarray(data[select_valylist])

        st.subheader("Valores de Interes")
        vals = st.text_input("Los valores se separan por coma")
        List_Val = lambda x : [int(i) for i in re.split(",",x) if i!=""]
        arraylist = List_Val(vals)
        valInit= list(map(float,arraylist))

        #Gaussian Classification configuration
        gnb = GaussianNB()
        gnb.fit(X, Y)
        prediction = gnb.predict([valInit])

        st.write("---- Prediccion: ")
        st.write(prediction)
