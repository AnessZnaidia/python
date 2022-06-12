#on import les librairies nécéssaires au bon fonctionnement du code

import streamlit as st 
import pandas as pd 
import plotly_express as px
import plotly.graph_objects as go
#import mymodel as m 

st.set_page_config(page_title = 'Web App sur le COVID 19', layout="wide")

#début de la création du dashboard avec le titre notamment

st.title("Bienvenue sur le Dashboard Intéractif des Données liées à la Pandémie du Covid 19 en France")
#st.write("""
# COVID-19 Dashboard
#Below you will find our dashbord that is updated every day.
#""")


#my_expander = st.expander(label='Expand me')
#my_expander.write('Hello there!')
#clicked = my_expander.button('Click me!')

#importation des datasets via le site data.gouv.fr (les données sont mises à jour quotidiennement)

df = pd.read_csv('https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19/20210202-220106/vaccination-regional.csv', sep = ',')
df['date'] = pd.to_datetime(df['date'])
#st.line_chart(df.plot())
df['jour_semaine'] = df['date'].dt.day_name()
df['total_deaths'] = 10

#state_data = df[df['nom'] == chosen_reg]
#fig3 = px.bar(state_data, x='jour_semaine', y=chosen_count)
#boxplot_chart = st.plotly_chart(fig3)

#selectbox = st.sidebar.selectbox(
    #"Select the one you want",
    #["Vaccinated", "Not Vacinnated"]
#)
#st.write(f"You selected {selectbox}")

#fig2 = px.line(df, x='jour', y='nb')
#ts_chart = st.plotly_chart(fig2)

df2 = pd.read_csv('https://static.data.gouv.fr/resources/donnees-des-urgences-hospitalieres-et-de-sos-medecins-relatives-a-lepidemie-de-covid-19/20220610-190111/sursaud-covid-quot-reg-2022-06-10-19h01.csv', sep = ';')

#df2

df2['date_de_passage'] = pd.to_datetime(df2['date_de_passage'])
df2['jour_semaine'] = df2['date_de_passage'].dt.day_name()
df2['Mois'] = pd.DatetimeIndex(df2['date_de_passage']).month
df2['Mois'] = df2['Mois'].replace([1],'Janvier')
df2['Mois'] = df2['Mois'].replace([2],'Février')
df2['Mois'] = df2['Mois'].replace([3],'Mars')
df2['Mois'] = df2['Mois'].replace([4],'Avril')
df2['Mois'] = df2['Mois'].replace([5],'Mai')
df2['Mois'] = df2['Mois'].replace([6],'Juin')
df2['Mois'] = df2['Mois'].replace([7],'Juillet')
df2['Mois'] = df2['Mois'].replace([8],'Août')
df2['Mois'] = df2['Mois'].replace([9],'Septembre')
df2['Mois'] = df2['Mois'].replace([10],'Octobre')
df2['Mois'] = df2['Mois'].replace([11],'Novembre')
df2['Mois'] = df2['Mois'].replace([12],'Décembre')
df2['jour_semaine'] = df2['jour_semaine'].replace('Monday','Lundi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Tuesday','Mardi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Wednesday','Mercredi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Thursday','Jeudi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Friday','Vendredi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Saturday','Samedi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Sunday','Dimanche')



#fig3 = px.bar(df2, x='jour_semaine', y='hosp')
#barplot_chart = st.plotly_chart(fig3)


df3 = pd.read_csv('https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/20220610-190150/vacsi-s-a-reg-2022-06-10-19h01.csv', sep = ';')

#remplacement des valeurs par les noms des département associés

df3['reg'] = df3['reg'].replace([1],'Guadeloupe')
df3['reg'] = df3['reg'].replace([2],'Martinique')
df3['reg'] = df3['reg'].replace([3],'Guyane')
df3['reg'] = df3['reg'].replace([4],'La Réunion')
df3['reg'] = df3['reg'].replace([11],'Ile-de-France')
df3['reg'] = df3['reg'].replace([24],'Centre-Val de Loire')
df3['reg'] = df3['reg'].replace([27],'Bourgogne-Franche-Comté')
df3['reg'] = df3['reg'].replace([23],'Normandie')
df3['reg'] = df3['reg'].replace([32],'Hauts-de-France')
df3['reg'] = df3['reg'].replace([44],'Grand Est')
df3['reg'] = df3['reg'].replace([52],'Pays de la Loire')
df3['reg'] = df3['reg'].replace([53],'Bretagne')
df3['reg'] = df3['reg'].replace([75],'Nouvelle-Acquitaine')
df3['reg'] = df3['reg'].replace([76],'Occitanie')
df3['reg'] = df3['reg'].replace([84],'Auvergne-Rhône-Alpes')
df3['reg'] = df3['reg'].replace([93],"Provence-Alpes-Côte d'Azur")
df3['reg'] = df3['reg'].replace([94],'Corse')
df3['reg'] = df3['reg'].replace([5],'Saint-Pierre-et-Miquelon')
df3['reg'] = df3['reg'].replace([6],'Mayotte')
df3['reg'] = df3['reg'].replace([7],'Saint-Barthélemy')
df3['reg'] = df3['reg'].replace([8],'Saint-Martin')

#remplacement des valeurs par les tranches d'âges asscoiées

df3['clage_vacsi'] = df3['clage_vacsi'].replace([4],'0-4 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([11],'10-11 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([17],'12-17 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([24],'18-24 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([29],'25-29 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([39],'30-39 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([49],'40-49 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([9],'5-9 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([59],'50-59 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([64],'60-64 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([69],'65-69 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([74],'70-74 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([79],'75-79 ans')
df3['clage_vacsi'] = df3['clage_vacsi'].replace([80],'80 ans et plus')


df4 = pd.read_csv('https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/20220610-190159/vacsi-tot-v-reg-2022-06-10-19h01.csv', sep = ';')


df4['vaccin'] = df4['vaccin'].replace([1],'Pfizer Adulte')
df4['vaccin'] = df4['vaccin'].replace([2],'Moderna')
df4['vaccin'] = df4['vaccin'].replace([3],'AstraZeneka')
df4['vaccin'] = df4['vaccin'].replace([4],'Janssen')
df4['vaccin'] = df4['vaccin'].replace([5],'Pfizer Enfant')
df4['vaccin'] = df4['vaccin'].replace([6],'Novavax')

indexNames2 = df4[ df4['vaccin'] == 0 ].index
df4.drop(indexNames2 , inplace=True)

df4['reg'] = df4['reg'].replace([1],'Guadeloupe')
df4['reg'] = df4['reg'].replace([2],'Martinique')
df4['reg'] = df4['reg'].replace([3],'Guyane')
df4['reg'] = df4['reg'].replace([4],'La Réunion')
df4['reg'] = df4['reg'].replace([11],'Ile-de-France')
df4['reg'] = df4['reg'].replace([24],'Centre-Val de Loire')
df4['reg'] = df4['reg'].replace([27],'Bourgogne-Franche-Comté')
df4['reg'] = df4['reg'].replace([23],'Normandie')
df4['reg'] = df4['reg'].replace([32],'Hauts-de-France')
df4['reg'] = df4['reg'].replace([44],'Grand Est')
df4['reg'] = df4['reg'].replace([52],'Pays de la Loire')
df4['reg'] = df4['reg'].replace([53],'Bretagne')
df4['reg'] = df4['reg'].replace([75],'Nouvelle-Acquitaine')
df4['reg'] = df4['reg'].replace([76],'Occitanie')
df4['reg'] = df4['reg'].replace([84],'Auvergne-Rhône-Alpes')
df4['reg'] = df4['reg'].replace([93],"Provence-Alpes-Côte d'Azur")
df4['reg'] = df4['reg'].replace([94],'Corse')
df4['reg'] = df4['reg'].replace([5],'Saint-Pierre-et-Miquelon')
df4['reg'] = df4['reg'].replace([6],'Mayotte')
df4['reg'] = df4['reg'].replace([7],'Saint-Barthélemy')
df4['reg'] = df4['reg'].replace([8],'Saint-Martin')


#suppression de la ligne qui correspond à 'tous les âges'

indexNames = df3[ df3['clage_vacsi'] == 0 ].index
df3.drop(indexNames , inplace=True)

#création d'une colonne 'Année'

df3['Année'] = pd.DatetimeIndex(df3['jour']).year
df4['Année'] = pd.DatetimeIndex(df4['jour']).year
df2['Année'] = pd.DatetimeIndex(df2['date_de_passage']).year



#renommer les noms des colonnes qui nous intéréssent

df3.rename(columns={'reg': 'Région', 
                    'clage_vacsi': 'Tranche Age',
                    'n_complet_h' : 'Homme',
                    'n_complet_f' : 'Femme', 
                     'n_dose1_h': 'Nombre de vaccins'},inplace=True)

#création des sliders pour filtrer les données selon l'utilisateur

choix_annee = st.sidebar.selectbox(
   'Veuillez choisir une année',
   [2021,2022]
)

choix_region = st.sidebar.selectbox(
   'Veuillez choisir une région',
   df3['Région'].unique()
)

c1, c2 = st.columns((2.5,2.5))

with c1 :
   donnee_choisies3 = df2[df2['Année'] == choix_annee]

   donnee_choisies3 = donnee_choisies3.groupby('Mois').sum()

   donnee_choisies3 = donnee_choisies3.reset_index()

   fig4 = go.Figure()

   area_one = go.Scatter(name = "Homme", x=donnee_choisies3['Mois'], y=donnee_choisies3['nbre_hospit_corona_h'], stackgroup = 'one')
   area_two = go.Scatter(name = 'Femme',x=donnee_choisies3['Mois'],y=donnee_choisies3['nbre_hospit_corona_f'],stackgroup = 'one')


   fig4.add_trace(area_one)
   fig4.add_trace(area_two)


   fig4.update_layout(xaxis_type = 'category', title_text="Evolution des personnes hospitalisées pour le COVID 19 le selon le mois")

   fig4.update_xaxes(categoryorder = 'array', categoryarray= ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 
   'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], title = 'Mois')

   fig4.update_yaxes(title = 'Nombre de personnes')

   ts_chart = st.plotly_chart(fig4)



   #filtration des données pour la création du pie chart
   donnee_choisies = df3[(df3['Région'] == choix_region) & (df3['Année'] == choix_annee)]

   fig = px.pie(donnee_choisies, values='Nombre de vaccins', names='Tranche Age', 
   title="Pie Chart du Nombre de Vaccins par Tranche d'Age")
   pie_chart = st.plotly_chart(fig)

   donnee_choisies2 = df4[(df4['reg'] == choix_region) & (df4['Année'] == choix_annee)]

   fig3 = px.bar(donnee_choisies2, x='vaccin', y='n_tot_dose3', title="Nombre de Dose pour Chacun des Différents Type de Vaccin (2022)")
   bar_chart = st.plotly_chart(fig3)




with c2:

   if choix_annee == 2021:

      fig5 = px.line(donnee_choisies3, x=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 
      'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], y='nbre_pass_corona',markers=True, title = 'Evolution du nombre de passages aux urgences pour le COVID 19 selon le mois', labels=
      {'x':'Mois', 'nbre_pass_corona':'Nombre de personnes'})

      line_chart = st.plotly_chart(fig5)
   else:

      fig5 = px.line(donnee_choisies3, x=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin'], y='nbre_pass_corona',markers=True, title = 'Evolution du nombre de passages aux urgences pour le COVID 19 selon le mois', labels=
      {'x':'Mois', 'nbre_pass_corona':'Nombre de personnes'})

      line_chart = st.plotly_chart(fig5)


   #filtration des données pour la création du donut chart
   labels = ['Homme', 'Femme']
   values = [donnee_choisies['Homme'].sum(), donnee_choisies['Femme'].sum()]

   fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
   donut_chart = st.plotly_chart(fig2)
