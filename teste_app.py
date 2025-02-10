import streamlit as st
import warnings
from pandas.errors import SettingWithCopyWarning
from home import HomePage
from model import ModelPage
from history import HistoryPage
from forecast_class import Forecast


st.write("teste")

lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista corretamente
lista_de_compras.append("Ovos")
st.write("Item adicionado: Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")
st.write("Item removido: Banana")

# Exibindo a lista formatada
st.write("Lista de Compras Atualizada:")
st.write(lista_de_compras)

