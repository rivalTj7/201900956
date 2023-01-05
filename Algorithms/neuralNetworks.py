#web site 
import streamlit as st
#Maching learnign Imports
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report
#import numpy as np
import numpy as np
#Local Imports
from Records.File import File
#import plotly.express as px
import plotly.express as px

fil = File()

def neuraNetworks():
    st.header(f"Data Entry in Neural Networks")

    data = fil.OpenFile()
    if (data is not None):

        with st.form("entry_form", clear_on_submit=True):
            target_options = data.columns
            with st.expander("   Variables"):
                clas = st.selectbox("Seleccione la columna de clasificacion: ",(target_options)) 
                respo = st.multiselect("Seleccione la columna de Respuesta: ", (data.drop(columns=[clas]).columns)) 
            with st.expander("Valores de Interes"):
                vals = st.text_input("Valor a inspeccionar")

            submitted = st.form_submit_button("Save Data")
            
            if submitted:
                #Jalando los valores 
                X = data[respo]
                y = data[clas].values

                le = LabelEncoder()

                y = le.fit_transform(y.flatten())

                try:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
                except:
                    st.markdown('<span style="color:red">Error en la carga de datos <br /> cuando coloque datos en forma de vector coloquele la coma <br /> </span>', unsafe_allow_html=True)  
                
                #Configuracion de la red neuronal
                
                scaler = StandardScaler()  
                scaler.fit(X_train)
                X_train = scaler.transform(X_train)  
                X_test = scaler.transform(X_test)

                #Creando la red neuronal
                clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

                clf.fit(X_train, y_train)
                y_pred = clf.predict(X_test)
                score = accuracy_score(y_test, y_pred) * 100
                report = classification_report(y_test, y_pred)
                st.text("Precision del modelo: ")
                st.write(score,"%")
                fig = px.histogram(data[clas], x =clas)
                st.plotly_chart(fig)

                if vals != "":
                    #Guardar los valores
                    valuesPredict = np.array([])
                    for column in respo:
                        valuesPredict = np.append(valuesPredict, vals)
                    #Crear la prediccion
                    valuesPredict = valuesPredict.reshape(1,-1)
                    scaler = StandardScaler()  
                    scaler.fit(X_train)  
                    valuesPredict = scaler.transform(valuesPredict)	
                    pred = clf.predict(valuesPredict)
                    st.write("La prediccion es:  ", str(le.inverse_transform(pred)))


            """if submitted:

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
                    st.subheader(model.predict([map_obj]))"""