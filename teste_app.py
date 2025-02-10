import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import xgboost as xgb
import yfinance as yf
import pmdarima as pm
from prophet import Prophet

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

