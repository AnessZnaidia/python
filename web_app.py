# on import les librairies nécéssaires au bon fonctionnement du code

import streamlit as st 
import pandas as pd 
import plotly_express as px
import plotly.graph_objects as go
import datetime

# début de la création du dashboard avec le titre notamment

st.set_page_config(page_title = 'Web App sur le COVID 19', layout="wide")
st.title("Bienvenue sur le Dashboard Intéractif des Données liées à la Pandémie du Covid 19 en France")


# importation des datasets via le site data.gouv.fr (les données sont mises à jour quotidiennement ou chaque semaine)


df2 = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/d2af5160-a21d-47b7-8f30-3c20dade63b1', sep = ';')
df3 = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/8e5e70fa-c082-45e3-a7b8-20862711b142', sep = ';')
df4 = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/9b275b84-2caa-4815-8523-2f1451e6952b', sep = ';')
france_entiere = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/e3d83ab3-dc52-4c99-abaf-8a38050cc68c', sep = ';') 



## cleaning des différents datasets

# conversion des dates dans le bon format 

df2['date_de_passage'] = pd.to_datetime(df2['date_de_passage'])
df4['jour'] = pd.to_datetime(df4['jour'])


# création de la colonne jour_semaine

df2['jour_semaine'] = df2['date_de_passage'].dt.day_name()
df4['jour_semaine'] = df4['jour'].dt.day_name()

# création de la colonne mois 

df2['Mois'] = pd.DatetimeIndex(df2['date_de_passage']).month

# création d'une colonne 'Année'

df3['Année'] = pd.DatetimeIndex(df3['jour']).year
df4['Année'] = pd.DatetimeIndex(df4['jour']).year
df2['Année'] = pd.DatetimeIndex(df2['date_de_passage']).year
france_entiere['Année'] = pd.DatetimeIndex(france_entiere['jour']).year


# remplacement des bonnes valeurs avec le mois 

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

# remplacement des bonnes valeurs avec le jour 

df2['jour_semaine'] = df2['jour_semaine'].replace('Monday','Lundi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Tuesday','Mardi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Wednesday','Mercredi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Thursday','Jeudi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Friday','Vendredi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Saturday','Samedi')
df2['jour_semaine'] = df2['jour_semaine'].replace('Sunday','Dimanche')

df4['jour_semaine'] = df4['jour_semaine'].replace('Monday','Lundi')
df4['jour_semaine'] = df4['jour_semaine'].replace('Tuesday','Mardi')
df4['jour_semaine'] = df4['jour_semaine'].replace('Wednesday','Mercredi')
df4['jour_semaine'] = df4['jour_semaine'].replace('Thursday','Jeudi')
df4['jour_semaine'] = df4['jour_semaine'].replace('Friday','Vendredi')
df4['jour_semaine'] = df4['jour_semaine'].replace('Saturday','Samedi')
df4['jour_semaine'] = df4['jour_semaine'].replace('Sunday','Dimanche')


# remplacement des bonnes valeurs avec la région

df2['reg'] = df2['reg'].replace([1],'Guadeloupe')
df2['reg'] = df2['reg'].replace([2],'Martinique')
df2['reg'] = df2['reg'].replace([3],'Guyane')
df2['reg'] = df2['reg'].replace([4],'La Réunion')
df2['reg'] = df2['reg'].replace([11],'Ile-de-France')
df2['reg'] = df2['reg'].replace([24],'Centre-Val de Loire')
df2['reg'] = df2['reg'].replace([27],'Bourgogne-Franche-Comté')
df2['reg'] = df2['reg'].replace([23],'Normandie')
df2['reg'] = df2['reg'].replace([32],'Hauts-de-France')
df2['reg'] = df2['reg'].replace([44],'Grand Est')
df2['reg'] = df2['reg'].replace([52],'Pays de la Loire')
df2['reg'] = df2['reg'].replace([53],'Bretagne')
df2['reg'] = df2['reg'].replace([75],'Nouvelle-Acquitaine')
df2['reg'] = df2['reg'].replace([76],'Occitanie')
df2['reg'] = df2['reg'].replace([84],'Auvergne-Rhône-Alpes')
df2['reg'] = df2['reg'].replace([93],"Provence-Alpes-Côte d'Azur")
df2['reg'] = df2['reg'].replace([94],'Corse')
df2['reg'] = df2['reg'].replace([5],'Saint-Pierre-et-Miquelon')
df2['reg'] = df2['reg'].replace([6],'Mayotte')
df2['reg'] = df2['reg'].replace([7],'Saint-Barthélemy')
df2['reg'] = df2['reg'].replace([8],'Saint-Martin')

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

# remplacement des bonnes valeurs avec la tranche d'âge

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


# suppression de la ligne qui correspond à 'tous les âges'

indexNames = df3[ df3['clage_vacsi'] == 0 ].index
df3.drop(indexNames , inplace=True)

# remplacement des bonnes valeurs avec le type de vaccin 

df4['vaccin'] = df4['vaccin'].replace([1],'Pfizer Adulte')
df4['vaccin'] = df4['vaccin'].replace([2],'Moderna')
df4['vaccin'] = df4['vaccin'].replace([3],'AstraZeneka')
df4['vaccin'] = df4['vaccin'].replace([4],'Janssen')
df4['vaccin'] = df4['vaccin'].replace([5],'Pfizer Enfant')
df4['vaccin'] = df4['vaccin'].replace([6],'Novavax')

# suppression de la ligne qui correspond à 'tous les vaccins'

indexNames2 = df4[ df4['vaccin'] == 0 ].index
df4.drop(indexNames2 , inplace=True)

# renommer les noms des colonnes qui nous intéréssent

df3.rename(columns={'reg': 'Région', 
                    'clage_vacsi': 'Tranche Age',
                    'n_complet_h' : 'Homme',
                    'n_complet_f' : 'Femme', 
                     'n_dose1_h': 'Nombre de vaccins'},inplace=True)


# remplacer les données manquantes avec des 0

france_entiere['PourAvec'] = france_entiere['PourAvec'].fillna(0)

## input data pour le choix de la période entre 2 dates 

# obtenir la date du jour où l'utilisateur est sur le dashboard

aujourdhui = datetime.date.today() 

# choisir comme date de fin 7 jour avant la date du jour 

j_7 = aujourdhui - datetime.timedelta(days=14)

# création du sidebar (partie gauche du daschboard)

st.sidebar.write('Le choix des deux dates juste en dessous concerne le premier graphique, celui des données sur toute la France')
jour1 = st.sidebar.date_input("Veuillez choisir la date de début d'analyse", j_7)
jour2 = st.sidebar.date_input("Veuillez choisir la date de fin d'analyse", aujourdhui)
if jour1 < jour2:
    st.sidebar.success("Les dates choisies se suivent, l'analyse peut être faite :)")
else:
    st.sidebar.error('Erreur: la date de fin doit suivre la date de départ :(')

# création des sliders pour filtrer les données selon l'utilisateur

st.sidebar.write("Les deux variables déroulantes s'appliquent sur tous les graphiques à l'exception du premier")
choix_annee = st.sidebar.selectbox(
   'Veuillez choisir une année',
   [2021,2022]
)

choix_region = st.sidebar.selectbox(
   'Veuillez choisir une région',
   df3['Région'].unique()
)

### début de l'implémentation des graphiques sur le dashboard 

# création du layout du dashboard : 2 colonnes avec les graphiques, 3 graphiques dans chaque colonne
c1, c2 = st.columns((2.5,2.5))


# colonne 1 : c1
with c1 :

   # sélection des données à propos du covid (1 dans le dataset) et en fonction des paramètres de l'utilisateur

   donnees_plot1 = france_entiere[(france_entiere['PourAvec'] == 1) & (france_entiere['jour'] >= str(jour1)) & (france_entiere['jour'] <= str(jour2))]

   # on groupe les données par jour et on fait la somme

   donnees_plot1 = donnees_plot1.groupby('jour').sum()

   #on reset l'index du dataset pour plus de faciliter

   donnees_plot1 = donnees_plot1.reset_index()

   # plot du premier graphique de la colonne c1 : line chart

   fig1 = px.line(donnees_plot1, x='jour', y='tx_prev_SC',markers=True, 
   title="Evolution du taux de personnes en soins critiques pour le COVID 19 en France", 
   labels = {'jour':'Date', 'tx_prev_SC' :'Taux (pour 100 000 hab)'}) 
   fig1.update_traces(line_color='red')
   line_chart = st.plotly_chart(fig1)

   # filtration des données pour la création du pie chart

   donnees_plot2 = df3[(df3['Région'] == choix_region) & (df3['Année'] == choix_annee)]

   # plot du second graphique de la colonne c1 : pie chart 

   fig2 = px.pie(donnees_plot2, values='Nombre de vaccins', names='Tranche Age', 
   title="Nombre de vaccins par tranche d'age (gauche) et par genre (droite) selon l'année et la région")
   pie_chart = st.plotly_chart(fig2)

   # filtration des données pour la création du bar chart

   donnees_plot3 = df4[(df4['reg'] == choix_region)]

   # plot du troisième graphique de la colonne c1 : bar chart 

   fig3 = px.bar(donnees_plot3, x='vaccin', y='n_tot_dose3', title="Nombre de personnes ayant les 3 doses pour chaque type de vaccin selon la région (2022)", 
   labels = {'vaccin':'Type de vaccin',
   'n_tot_dose3':"Nombre de personnes ayant les 3 doses"})
   bar_chart = st.plotly_chart(fig3)


# colonne 2 : c2
with c2:

   # sélection des données selon l'année choisie par l'utilisateur

   donnees_plot4 = df2[df2['Année'] == choix_annee]

   # on groupe les données par jour et on fait la somme

   donnees_plot4 = donnees_plot4.groupby('Mois').sum()

   # on reset l'index du dataset pour plus de faciliter

   donnees_plot4 = donnees_plot4.reset_index()

   # on nettoie la colonne des données souhaitées en remplacant le 'k' par 10**3 et on calcule la valeur correspondante

   donnees_plot4['nbre_hospit_corona_h'] = donnees_plot4['nbre_hospit_corona_h'].astype(str).replace({'k': '*1e3'}, regex=True).map(pd.eval).astype(float)
   donnees_plot4['nbre_hospit_corona_f'] = donnees_plot4['nbre_hospit_corona_f'].astype(str).replace({'k': '*1e3'}, regex=True).map(pd.eval).astype(float)


   # plot du premier graphique de la colonne c2 : area chart

   fig5 = go.Figure()
   fig5.add_trace(go.Scatter(name='Femme', x=donnees_plot4['Mois'],y=donnees_plot4['nbre_pass_corona_f'], stackgroup='one', mode='lines'))
   fig5.add_trace(go.Scatter(name = "Homme", x=donnees_plot4['Mois'], y=donnees_plot4['nbre_pass_corona_h'], stackgroup='two', mode='lines'))
   fig5.update_layout(xaxis_type = 'category', title_text="Evolution des personnes hospitalisées pour le COVID 19 selon le mois en France")
   fig5.update_xaxes(categoryorder = 'array', categoryarray= ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 
   'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], title = 'Mois')
   fig5.update_yaxes(title = 'Nombre de personnes', tickformat = "digit")

   aera_chart = st.plotly_chart(fig5)

   # filtration des données pour la création du donut chart

   labels = ['Homme', 'Femme']
   values = [donnees_plot2['Homme'].sum(), donnees_plot2['Femme'].sum()]

   # plot du deuxième graphique de la colonne c2 : donut chart

   fig6 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
   donut_chart = st.plotly_chart(fig6)

   # filtration des données pour la création du violin chart

   donne_vio = df2[(df2['Année'] == choix_annee) & (df2['reg'] == choix_region)]

   # plot du 3ème graphique de la colonne c2 : violin chart

   fig6 = go.Figure()
   jour_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
   for jour in jour_semaine:
      fig6.add_trace(go.Violin(x=donne_vio['jour_semaine'][donne_vio['jour_semaine'] == jour],
                              y=donne_vio['nbre_hospit_corona'][donne_vio['jour_semaine'] == jour],
                              name=jour,
                              box_visible=False,
                              meanline_visible=True))


   fig6.update_layout(title_text="Nombre d'hospitalisation pour le COVID 19 selon le jour de la semaine")   
   fig6.update_xaxes(title = 'Jour de la semaine')
   fig6.update_yaxes(title = 'Nombre de personnes')
   violin_chart = st.plotly_chart(fig6)
