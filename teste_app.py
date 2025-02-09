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
