#streamlit rappel données fictives: 
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

#Données fictives
data = {
    "profil":["VIP", "Promo addict", "Régulier", "Occasionnel"],
    "nb_clients":[28, 19, 32, 21],
    "nb_commandes":[1600,1728,1485,792],
    "panier_moyen":[650.12, 550.20, 510.00, 420.40],
    "ratio_code_promos":[0.68,0.82,0.65,0.72],
    "chiffre_affaires":[102000, 95000, 78000, 32000]

}

#Création du dataframe
df=pd.DataFrame(data)

st.title("Dashboard comportement clients")
st.subheader("Tableau comparatif des KPIs")
st.dataframe(df.style.highlight_max(axis=0))

#Camembert profils
st.subheader("Répartition des profils")
fig1,ax1=plt.subplots()
df.set_index("profil")["nb_clients"].plot(kind="pie",autopct="%1.1f%%",startangle=90,ax=ax1)
st.pyplot(fig1)

#Graphiques en barre pour les chiffres d'affaires par rapport aux profils
fig2,ax2=plt.subplots()
df.sort_values("chiffre_affaires",ascending=True).plot(kind="barh",x="profil",y="chiffre_affaires",color="salmon",ax=ax2)
st.pyplot(fig2)

#Panier moyen par profil
st.subheader("Panier moyen par profil")
fig3,ax3=plt.subplots()
df.sort_values("panier_moyen",ascending=True).plot(kind="barh",x="profil",y="panier_moyen",color="skyblue",ax=ax3)
st.pyplot(fig3)


st.markdown("**Projet e-commerce réalisé en autonomie par Mejrissi Yasmine**")
