#Maching learnign Imports
import streamlit as st
import numpy as np
from sklearn.neural_network import MLPClassifier
#Local Imports
from Records.File import File
import re

fil = File()

def neuraNetworks():
    st.header(f"Data Entry in Neural Networks")

    data = fil.OpenFile()
    if (data is not None):

        with st.form("entry_form", clear_on_submit=True):
            clas = st.selectbox("Seleccione la columna de clasificacion: ", data.keys())
            respo = st.selectbox("Seleccione la columna de Respuesta: ", data.keys())

            st.write("Valores de Interes")
            vals = st.text_input("Separar por coma")
            
            submitted = st.form_submit_button("Save Data")
            
            if submitted:
                X = np.asarray(data[clas]).reshape(-1, 1)
                Y = data[respo]
                if vals != "":
                    List_Val = lambda x : [int(i) for i in re.split(",",x) if i!=""]
                    arraylist = List_Val(vals)
                    valInit= list(map(float,arraylist))
                
                #Decision Tree configuration
                clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=1, max_iter=200)
                
                #Train
                clf.fit(X,Y)
                
                #Predict
                if vals != "":
                    print("Vals si tiene datos aaaaaaaaaaaaaaaaaaaaa...................",vals)
                    st.write("Prediccion: ")
                    st.write(clf.predict([valInit]))
                else:
                    st.write("Prediccion: ")
                    st.write(clf.predict(X))