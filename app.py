# Importer les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger le dataset
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

file_path = "BeansDataSet.csv"  # Chemin vers votre dataset
beans_data = load_data(file_path)

# Titre de l'application
st.title("Application d'Analyse des Données - Beans and Pods")

# Section 1 : Aperçu des données
st.header("Aperçu des Données")
st.write("Voici un aperçu des premières lignes de votre dataset :")
st.dataframe(beans_data.head())

# Section 2 : Visualisation des Ventes Totales par Produit
st.header("Ventes Totales par Produit")
total_sales_by_product = beans_data[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].sum()

# Afficher les données sous forme de tableau
st.write("Ventes Totales par Produit :")
st.write(total_sales_by_product)

# Graphique interactif
st.subheader("Graphique des Ventes Totales par Produit")
fig, ax = plt.subplots(figsize=(10, 6))
total_sales_by_product.plot(kind='bar', ax=ax)
ax.set_title("Ventes Totales par Produit")
ax.set_xlabel("Produit")
ax.set_ylabel("Ventes Totales")
st.pyplot(fig)

# Section 3 : Analyse par Canal et Région
st.header("Analyse des Ventes par Canal et Région")
selected_channel = st.selectbox("Choisissez un canal :", beans_data["Channel"].unique())
selected_region = st.selectbox("Choisissez une région :", beans_data["Region"].unique())

filtered_data = beans_data[(beans_data["Channel"] == selected_channel) & (beans_data["Region"] == selected_region)]

st.write(f"Ventes filtrées pour le canal **{selected_channel}** et la région **{selected_region}** :")
st.dataframe(filtered_data)

# Graphique pour les données filtrées
st.subheader("Graphique des Ventes Filtrées")
channel_region_sales = filtered_data[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].sum()

fig, ax = plt.subplots(figsize=(10, 6))
channel_region_sales.plot(kind='bar', ax=ax)
ax.set_title(f"Ventes Totales pour {selected_channel} - {selected_region}")
ax.set_xlabel("Produit")
ax.set_ylabel("Ventes Totales")
st.pyplot(fig)

# Footer
st.write("Créé avec ❤️ par Rihame")
