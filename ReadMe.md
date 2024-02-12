# World Hapinness Report 🌎️

## Introduction

Bienvenue dans votre rapport sur les données "World Hapinness" ! Dans cette application streamlit, vous pourrez naviguer 
à travers ces données via des graphiques interactifs ainsi que des tableaux de détails pour chaque pays.


## Comment Exécuter

Pour exécuter l'application, deux possibilités : 

1. Vous pouvez récupérer l'image docker via dockerhub et la commande suivante : 
    ```bash
    docker pull axelfritz2/world_hapiness_report
    ```

2. Sinon vous pouvez créer l'image docker via le docker file de ce repository en suivant ces étapes : 

   1. Cloner le repository de l'application : 

       ```bash
       git clone https://github.com/AxelFritz2/Projet_Linux.git
       ```

   2. Accéder au répertoire : 
       ```bash
       cd Projet_Linux
       ```

   3. Créer l'image Docker :

       ```bash
       docker build -t application:latest .
       ```

En créant l'image docker, un environnement virtuel va se créer et les dépendances vont se télécharger directement. 
## Utilisation

Pour lancer l'application, il vous suffit de lancer la commande Docker run. Si vous avez récupéré l'image docker via DockerHub :  
```bash
docker run -p 8501:8501 axelfritz2/world_hapiness_report
```

Si vous avez créé l'image via le docker file :
```bash
docker run -p 8501:8501 application
```

Cette commande va effectuer les tâches suivantes : 
- Télecharger les données .
- Mettre en forme les données pour l'application.
- Lancer l'application streamlit.

Vous pourrez ainsi lancer l'application via l'url **externe** fourni.

## Auteurs

- [Samuel Baheux](https://github.com/SamuelBaheux)
- [Samuel Launay Pariente](https://github.com/samuel-LP)
- [Axel Fritz](https://github.com/AxelFritz1)