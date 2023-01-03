#Crear la pagina princial del Frontend
from streamlit_option_menu import option_menu
#web server import
import streamlit as st
#Importing the libraries
import Algorithms.linearRegres as linearRegres
import Algorithms.polynomialReg as polynomialReg
import Algorithms.gaussianClas as gaussianClas
import Algorithms.neuralNetworks as neuralNetworks
import Algorithms.decisionTreeClas as decisionTreeClas

def main():
    # --------------------- SETTINGS ---------------------
    page_title = "Machine Learning"
    page_icon = ":smile:"

    #Crear el Titulo
    st.set_page_config(
        page_title = page_title,
        page_icon = page_icon
    )

    #Crear el Header
    hiden_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>
    """
    st.markdown(hiden_menu_style, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
            span[data-baseweb="tag"] {
                background-color: blue !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
    st.write("# Machine Learning" + page_icon)

    # --- HIDE STREAMLIT STYLE ---
    hide_st_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # --- NAVIGATION MENU ---
    selected = option_menu(
        menu_title = "Menú",
        options=["Regresion Lineal", "Regresion Polinomial","Clasificador Gausiano", "Clasificador de arboles de desicion","Redes neuronales"],
        icons=["pencil-fill", "bar-chart-fill",'list', 'bar-chart', 'graph-down'],  # https://icons.getbootstrap.com/
        orientation="horizontal",
    )

    # --- PAGES ---
    if selected == "Regresion Lineal":
        linearRegres.regresion_lineal()
    elif selected == "Regresion Polinomial":
        polynomialReg.polynomialReg()
    elif selected == "Clasificador Gausiano":
        gaussianClas.gaussianClas()
    elif selected == "Clasificador de arboles de desicion":
        decisionTreeClas.decisionTree()
    elif selected == "Redes neuronales":
        neuralNetworks.neuraNetworks()

if __name__ == '__main__':
    main()