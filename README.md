proyecto base con poetry, docker, cronjob, typer, postgres

## Asegúrate de que Typer y Poetry estén instalados en tu entorno de desarrollo.
## Si no los tienes instalados, puedes hacerlo con los siguientes comandos:

    pip install poetry

## si ya se tienen el proyecto clonado instalar las dependencias con el comando

    cd typer_poetry_example

    poetry install

## Creación de un proyector nuevo con typer

    poetry typer_poetry_example

    cd typer_poetry_example

    poetry add typer

## activa el entorno 

    cd typer_poetry_example

    poetry shell 

## ejecutar el proyecto

    poetry run python main.py crear-item "--nuevo item"

    poetry run python main.py listar-items  

## Ejecución con docker

    sudo docker build -t my-typer-app .
    
    sudo docker run -d my-typer-app