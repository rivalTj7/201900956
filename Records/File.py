#Importing the libraries
import streamlit as st
#Maching learnign Imports
import pandas as pd

#importo otra page
class File:
    def __init__(self):
        pass

    def OpenFile(self) -> pd.DataFrame:
        uploaded_file = st.file_uploader(label = "Sube tu archivos.",type=['csv','xls','xlsx','json'])
        if uploaded_file is not None:
            Filname = uploaded_file.name
            vext = Filname.split('.')
            extension= vext[1]
            try:
                if extension == 'csv':
                    dataframe = pd.read_csv(uploaded_file)
                    st.dataframe(dataframe)

                elif extension == 'xls':
                    dataframe = pd.read_excel(uploaded_file)
                    st.dataframe(dataframe)

                elif extension == 'xlsx':
                    dataframe = pd.read_excel(uploaded_file)
                    st.dataframe(dataframe)
                elif extension == 'json':
                    dataframe = pd.read_json(uploaded_file)
                    st.dataframe(dataframe)
                return dataframe
            except Exception as e: 
                print(e)
                st.subheader('Error al cargar archivo: ',e)
                return None