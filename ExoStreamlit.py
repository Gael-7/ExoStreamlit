import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Charger la base de données Iris
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target_name'] = df['target'].map({i: name for i, name in enumerate(iris.target_names)})
    return df

# Charger les données
data = load_data()

# Titre de l'application
st.title("Exploration et visualisation de la base de données Iris")

# Afficher les données
st.subheader("Tableau des données Iris")
st.dataframe(data)

# Affichage des informations générales
st.subheader("Informations générales")
st.write(data.info())

# Statistiques descriptives
if st.checkbox("Afficher les statistiques descriptives"):
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

# Graphique de distribution
st.subheader("Graphiques de distribution")
selected_column = st.selectbox(
    "Sélectionnez une colonne pour voir la distribution",
    options=data.columns[:-2]
)
fig, ax = plt.subplots()
sns.histplot(data[selected_column], kde=True, ax=ax)
st.pyplot(fig)

# Graphique en nuage de points (scatter plot)
st.subheader("Nuage de points")
x_axis = st.selectbox("Sélectionnez l'axe X", data.columns[:-2])
y_axis = st.selectbox("Sélectionnez l'axe Y", data.columns[:-2])

fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_axis, y=y_axis, hue="target_name", palette="Set2", ax=ax)
st.pyplot(fig)

# Matrice de corrélation avec heatmap
if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Matrice de corrélation")
    corr_matrix = data.iloc[:, :-2].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
