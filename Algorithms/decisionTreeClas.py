#Maching learnign Imports
import streamlit as st;
import numpy as np;
import matplotlib.pyplot as plt;
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, plot_tree
#Local Imports
from Records.File import File;

fil = File()

def decisionTree():
    st.header(f"Data Entry in Decision Tree")

    data =  fil.OpenFile()
    if (data is not None):


        with st.form("entry_form", clear_on_submit=True):
            with st.expander("   Variables"):
                varX = st.text_input("Valores de columna de interes", "Ej: val1, val2, val3....valn")
                varY = st.text_input("Ingrese el nombre del parametro Y", "")
            #No seleccionar ninguna columna
            cheNone = st.checkbox('No seleccionar ninguna columna')

            #Enviar datos
            submitted = st.form_submit_button("Save Data")

            if submitted:
                if cheNone:
                    data.columns = range(data.shape[1])
                    #Convert to array
                    X = np.array(data)
                    index = X.shape[1]
                    X = np.delete(X, int(index) - 1, axis=1)
                    #Index of Y
                    P = np.array(data)
                    P = P.T[int(index) - 1]
                    lista = []
                    #Remove the last column
                    for i in range(1, len(X.T.tolist())):
                        lista.append(data.iloc[:, int(i)].values)
                    features = list(zip(*lista))
                    #Decision Tree configuration
                    st.set_option('deprecation.showPyplotGlobalUse', False)
                    clf = DecisionTreeClassifier().fit(features, P)
                    plot_tree(clf, filled=True)
                    plt.show()
                    st.pyplot()
                else:
                    if varY != "":
                        X = varX.split(sep=',')
                        le = preprocessing.LabelEncoder()
                        array2=[]
                        for array1 in X:
                            array2.append(le.fit_transform(data[array1].to_numpy()))
                        
                        Xaux=list(zip(*array2))
                        Var_X = np.array(Xaux)
                        Var_Y = np.array(data[varY])

                        fig = plt.figure(figsize=(12,9))
                        clf= DecisionTreeClassifier().fit(Var_X, Var_Y)
                        plot_tree(clf,filled=True )
                        st.subheader("Grafica de arbol de decision")
                        st.pyplot(fig)
                    else:
                        y_val = data[varX]
                        data = data.drop([varX], axis=1)
                        x_val = []
                        label_encoder = preprocessing.LabelEncoder();
                        labels = data.head()
                        values = labels.columns

                        for val in values :
                            list_value = list(data[val])
                            transformation = label_encoder.fit_transform(list_value)
                            x_val.append(transformation)

                        features = list(zip(*x_val))
                        label = label_encoder.fit_transform(y_val)

                        clf = DecisionTreeClassifier().fit(features, label)
                        fig = plt.figure()
                        plt.style.use("bmh")
                        plot_tree(clf, filled=True)
                        plt.title("Tree Decition")

                        st.pyplot(fig)
