#nome = 'ALISON'
#print(f'Meu nome é : {nome}')
#lista = [1,'olá mundo',True,9.7]
#tupla = (1,'olá mundo',True,9.7)
# Criando uma lista de compras
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.write("teste")

lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
st.write(lista_de_compras.append("Ovos"))

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

st.write(lista_de_compras)
