#Maching learnign Imports
from sklearn.preprocessing import PolynomialFeatures
import streamlit as st;
import numpy as np;
import matplotlib.pyplot as plt;
from sklearn.linear_model import LinearRegression;
from sklearn.metrics import mean_squared_error, r2_score;
#Local Imports
from Records.File import File;

fil = File()

def polynomialReg():
    st.header(f"Data Entry in Polynomial Regression")

    #with open('style.css') as f:
    #    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    #Abrir archivo
    data =  fil.OpenFile()
    if (data is not None):
        dtf = data.columns.to_list()
        print(dtf)
        #Frame de seleccion de variables
        with st.form("entry_form", clear_on_submit=True):
            st.subheader("Select the variables to use in the analysis")
            #Caja de seleccion de variables
            with st.expander("   Variables"):
                index1, index2 = st.columns(2)
                index1 = st.selectbox("Seleccione X", (data.columns), index=0) 
                index2 = st.selectbox("Seleccione Y", (data.columns), index=1) 
            #Grado del polinomio
            with st.expander("   Grado del polinomio"):
                grado = st.number_input(
                    "Grado",
                    value=2,
                    help=""" Valor de grado de la funcion.""",
                )
            #Caja de texto para ingresar valor a predecir
            with st.expander("   Predict value"):
                val_prediccion = st.number_input('Ingrese valor', value=0)
            #Boton de envio
            submitted = st.form_submit_button("Save Data")

            if submitted:

                X = np.asarray(data[index1]).reshape(-1, 1)
                Y = data[index2]

                #Grado del polinomio
                poly = PolynomialFeatures(degree=int(grado))
                VX = poly.fit_transform(X)

                #Linear Regression
                linear_regression = LinearRegression()
                linear_regression.fit(VX, Y)
                Y_pred = linear_regression.predict(VX)
                error = np.sqrt(mean_squared_error(Y, Y_pred))
                r2 = r2_score(Y, Y_pred)

                # Prediccion
                if val_prediccion != 0:
                    x_min = val_prediccion
                    x_max = val_prediccion
                    new_x = np.linspace(x_min, x_max, 1)[:, np.newaxis]
                    VX = poly.fit_transform(new_x)
                    val_predict = linear_regression.predict(VX)

                # Grafica de resultados
                fig = plt.figure()
                plt.style.use("bmh")
                plt.scatter(X, Y, color="red")
                plt.plot(X, Y_pred, color="blue")
                plt.title(f"Polinomyal Regression with degree={grado}")
                plt.ylabel(index1)
                plt.xlabel(index2)

                # Configuracion de metricas

                with open('style.css') as f:
                    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
                st.markdown('### Metrics')
                col1, col2, col3 = st.columns(3)
                col1.metric("Error medio", round(error, 6))
                col2.metric("Coeficiente", round(linear_regression.coef_[grado], 6))
                col3.metric("R2", round(r2, 6))

                # Grafica
                st.pyplot(fig)

                # Funcion
                st.write("Funcion Polinomial:")
                zero = round(linear_regression.intercept_, 4);
                count = grado
                func = "f(x)="
                while count > 0:
                    func += f"{'' if linear_regression.coef_[count] < 0 else '+'}{round(float(linear_regression.coef_[count]), 8)}x{f'^{count}' if count != 1 else ''}"
                    count -= 1
                func += f"{'' if zero < 0 else '+'}{zero}"
                st.latex(func)
                
                # Print de la prediccion
                if (val_prediccion != 0):
                    st.write(f"Prediccion: ", "     " + str(val_predict).replace("[","").replace("]",""))
