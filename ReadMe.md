# Sentiment Recognition 👁️

## Introduction

Bienvenue dans votre rapport sur les données "World Hapinness" ! Dans cette application streamlit, vous pourrez naviguer 
à travers ces data via des visualisations graphiques ainsi que des tableaux.


## Comment Exécuter

Pour exécuter l'application, il faut créer un docker à partir du dockerfile. Voici les étapes :


1. Cloner le repository de l'application : 

    ```bash
    git clone https://github.com/AxelFritz2/Sentiment_Recognition.git
    ```

2. Accéder au répertoire : 
    ```bash
    cd Sentiment_Recognition
    ```

3. Créer l'image Docker :

    ```bash
    docker build -t application:latest .
    ```

En créant l'image docker, un environnement virtuel va se créer et les dépendances vont se télécharger directement. 
## Utilisation

Pour lancer l'application, il vous suffit de lancer la commande Docker run :

```bash
docker run application 
```

Cette commande va effectuer les tâches suivantes : 
- Télecharger les données d'entraînement depuis Kaggle (https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset)
- Entraîner le modèle de computer vision. 
- Lancer l'application streamlit

Vous pourrez ainsi lancer l'application via l'url fourni.

## Remarques

- La fonctionnalité de détection de sentiment peut ne pas fonctionner. Cette dernière est encore en cours développement. 
