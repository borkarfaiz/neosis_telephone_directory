# Neosis Telphone Directory
It is a telephone directory that lets users add their contacts in the system. and there are features to search and sort the contacts. user first must signup to use all the features.

**[Assignment Link](https://docs.google.com/document/d/1mxy4IsKZ0kdMWYs0mbH_PTC7HMzfp06Mv5alVZ3Yq4o/edit#)**

## Setting up the Project
- First, you should install the docker. **[Install Docker](https://docs.docker.com/engine/install/)**
- Build the docker image.
    ```bash
    sudo docker-compose -f local.yml build
    ```
- Run the container
    ```bash
    sudo docker-compose -f local.yml up -d
    ```
Congratulation all setup has been completed nothing more to setup.


## Some Commands for docker
 - Making migrations
     ```bash
     docker-compose -f production.yml run --rm django python manage.py makemigrations
     ```
 - For django shell
     ```bash
     docker-compose -f production.yml run --rm django python manage.py shell
     ```
 - For opening the bash
     ```bash
     docker-compose -f production.yml run --rm django bash
     ```
