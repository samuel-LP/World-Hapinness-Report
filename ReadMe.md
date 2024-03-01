# World Hapinness Report 🌎️

## Introduction

Welcome to your "World Happiness" data report! In this Streamlit application, you will be able to navigate through this data via interactive charts as well as detailed tables for each country.


## How to execute

To run the application, there are two possibilities: 

1. You can pull the Docker image from Docker Hub using the following command:

    ```bash
    docker pull samuel-LP/world_hapiness_report
    ```

2. Otherwise, you can create the Docker image using the Dockerfile from this repository by following these steps:

   1. Clone the repository of the application : 

       ```bash
       git clone git@github.com:samuel-LP/World-Hapinness-Report.git
       ```

   2. Access to the repository : 
       ```bash
       cd Projet_Linux
       ```

   3. Create the docker image:

       ```bash
       docker build -t application:latest .
       ```

While creating the Docker image, a virtual environment will be created and the dependencies will download directly.

## Utilisation

To launch the application, you just need to run the Docker run command. If you have pulled the Docker image via DockerHub:

```bash
docker run -p 8501:8501 samuel-LP/world-hapiness-report
```

If you have create the image via the docker file :

```bash
docker run -p 8501:8501 application
```

This command will perform the following tasks:

- Download the data.
- Format the data for the application.
- Launch the streamlit application.

You will thus be able to launch the application via the provided **external** URL.


## Authors

- [Samuel Baheux](https://github.com/SamuelBaheux)
- [Samuel Launay Pariente](https://github.com/samuel-LP)
- [Axel Fritz](https://github.com/AxelFritz1)
