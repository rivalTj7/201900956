#Maching learnign Imports
import pandas as pd
#Graphs imports
import plotly.graph_objects as go
#Importing the libraries
from Records.File import File
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt
import streamlit as st
import numpy as np

fil = File()

def regresion_lineal():
    #Header 
    st.header(f"Data Entry in Linear Regression")

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    #Abrir archivo
    data = fil.OpenFile()
    if (data is not None): 
        #Frame de seleccion de variables
        with st.form("entry_form", clear_on_submit=True):
            st.subheader("Select the variables to use in the analysis")

            with st.expander("Variables"):
                varX = st.selectbox('Seleccione X',  (data.columns), index=0) 
                varY = st.selectbox('Seleccione Y', (data.columns), index=1)

            #Caja de texto para ingresar valor a predecir
            with st.expander("Predict value"):
                val_prediccion = st.number_input('Ingrese valor', value=0)
            
            submitted = st.form_submit_button("Save Data")
            
            if submitted:
                varX = np.asarray(data[varX]).reshape(-1, 1)
                varY = data[varY]

                #Linear Regression configuration
                linear_regression = LinearRegression()
                linear_regression.fit(varX, varY)
                prediction = linear_regression.predict(varX)

                # Configuracion de metricas
                st.markdown('### Metrics')
                col1, col2, col3 = st.columns(3)
                col1.metric("Error medio", mean_squared_error(varY, prediction))
                col2.metric("Coeficiente", str(linear_regression.coef_))
                col3.metric("R2", r2_score(varY, prediction))

                st.set_option('deprecation.showPyplotGlobalUse', False)
                #Configuracion de grafica
                plt.scatter(varX, varY)
                plt.plot(varX, prediction, color='red')
                plt.show()
                st.pyplot()

                # Calcules
                slope = round(float(linear_regression.coef_), 4)
                intersection = round(float(linear_regression.intercept_), 4)

                st.write("### Tendency Function");
                st.latex(f"f(x)={slope}x {'+ ' if intersection>=0 else ''}{intersection}")

                #Prediccion
                if (val_prediccion != 0):
                    value_predict = linear_regression.predict([[val_prediccion]])
                    st.subheader("Prediction")
                    st.metric(f"The value is: ", value_predict, "-" if value_predict < 0 else "+")