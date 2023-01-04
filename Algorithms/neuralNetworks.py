#web site 
import streamlit as st
#Maching learnign Imports
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
import numpy as np
#Local Imports
from Records.File import File

fil = File()

def neuraNetworks():
    st.header(f"Data Entry in Neural Networks")

    data = fil.OpenFile()
    if (data is not None):

        with st.form("entry_form", clear_on_submit=True):
            with st.expander("   Variables"):
                clas = st.text_input("Seleccione la columna de clasificacion: ") 
                respo = st.text_input("Seleccione la columna de Respuesta: ") 
            with st.expander("Valores de Interes"):
                vals = st.text_input("Separar por coma")

            submitted = st.form_submit_button("Save Data")
            
            if submitted:

                if respo != "":
                    X = clas.split(sep =  ",")
                    le = preprocessing.LabelEncoder()
                    array2=[]
                    for array1 in X:
                        array2.append(le.fit_transform(data[array1].to_numpy()))
                    #Creacion de las variables de entrenamiento
                    Xaux=list(zip(*array2))
                    VarX = np.array(Xaux)
                    VarY = np.array(data[respo])
                    #Configuracion de la red neuronal
                    mlp=MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter=500, alpha=0.001, solver='adam', random_state=21, tol=0.00000001)
                    mlp.fit(VarX, VarY)

                    #Crear la prediccion
                    if vals != "":
                        listaPre = vals.split(sep=',')
                        map_obj = list(map(int,listaPre))
                        map_obj = np.array(map_obj)

                        predi= mlp.predict([map_obj])
                        st.subheader("Predicción de Tendencia")
                        st.success(predi)
                    elif vals == "" and respo != "":
                        st.write("Predictions")
                        predi= mlp.predict(VarX)
                        st.success(predi)
                else:
                    X = clas.split(sep =  ",")
                    le = preprocessing.LabelEncoder()
                    array2=[]
                    for array1 in X:
                        array2.append(le.fit_transform(data[array1].to_numpy()))
                    #Creacion de las variables de entrenamiento
                    Xaux=list(zip(*array2))
                    VarX = np.array(Xaux)

                    #variables y
                    listaPre = vals.split(sep=',')
                    VarY = list(map(int,listaPre))
                    VarY = np.array(VarY)

                    #Crear modelo
                    model = MLPClassifier(hidden_layer_sizes=(3,3,3),max_iter=1000)
                    lasso = linear_model.Lasso()
                    scores = cross_val_score(model,VarX,VarY)

                    st.text('Scores')
                    st.write(scores)
                    info = 'Score/puntuacion '+str(scores.mean())+' -Std. Desviacion '+str(scores.std())
                    st.subheader('Score')
                    st.text(info)


                    ## no incluir float ni palabras
                    listaPre = vals.split(sep=',')
                    map_obj = list(map(int,listaPre))
                    map_obj = np.array(map_obj)
                    print('arreglo de entrada: ',vars)
                    model.fit(VarX,VarY)
                    st.header('Resultado:')
                    st.subheader(model.predict([map_obj]))

