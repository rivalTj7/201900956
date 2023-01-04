import streamlit as st
import numpy as np
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from Records.File import File
import re

fil = File()
def gaussianClas():

    st.header(f"Data Entry in Gaussian Classification")

    data =  fil.OpenFile()
    if (data is not None):
        with st.form("entry_form", clear_on_submit=True):
            with st.expander("   Variables - Columna interes y respuesta"):
                select_valxlist = st.text_input("Valores de columna de interes", "Ej: val1, val2, val3....valn")
                select_valylist = st.selectbox('Valores de Columna de respuesta',(data.columns), index=1) 

            with st.expander("Valores de Interes"):
                vals = st.text_input("Los valores se separan por coma")

            #No seleccionar ninguna columna
            cheNone = st.checkbox('No seleccionar ninguna columna de interes ni de respuesta')

            submitted = st.form_submit_button("Save Data")

            if submitted:

                if cheNone:
                    if vals != "":
                        data.columns = range(data.shape[1])
                        X = np.array(data)

                        index = X.shape[1]
                        X = np.delete(X, int(index) - 1, axis=1)
                        play_column = np.array(data)
                        play_column = play_column.T[int(index) - 1]

                        lista_play = []
                        for i in play_column:
                            lista_play.append(i)
                        lt = X.T.tolist()
                        features = list(zip(*lt))
                        model = GaussianNB()
                        print("......................................................")
                        print(lista_play)
                        pre3 = np.array(lista_play).reshape(-1, 1)
                        print(features)
                        model.fit(features, pre3)
                        #Si o si tiene que tener por lo menos el predit
                        if vals != "":
                            cadena = vals.split(',')
                            entrada = [int(x) for x in cadena]
                            predicted = model.predict([entrada])
                            st.write("Predicción: ", predicted)
                    else:
                        st.error("No hay datos para predecir en la pestaña de valores de interes")
                else:
                    X = select_valxlist.split(",")
                    le = preprocessing.LabelEncoder()

                    array2=[]
                    for array1 in X:
                        array2.append(le.fit_transform(data[array1].to_numpy()))
                    
                    Xaux=list(zip(*array2))
                    VarX = np.array(Xaux)
                    VarY = np.array(data[select_valylist]) 

                    #Gaussian Classification configuration
                    gnb = GaussianNB()
                    gnb.fit(VarX, VarY)
                    print(VarY)
                    if vals != "":
                        listaPre = vals.split(sep=',')
                        print(listaPre)
                        pre2=[]
                        for li in listaPre:
                            pre2.append(float(li))
                        pre3 = np.array(pre2).reshape(-1, 1)
                        print(pre3)
                        st.subheader("Predicción de Tendencia")
                        st.success(gnb.predict(pre3))
                    else:
                        st.write("No hay valores para predecir, se predecira con los valores de la columna de interes")
                        st.write("Predicción de Tendencia")
                        st.success(gnb.predict(VarX))