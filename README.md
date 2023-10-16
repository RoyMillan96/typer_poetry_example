proyecto base con poetry, docker, cronjob, typer

## Asegúrate de que Typer y Poetry estén instalados en tu entorno de desarrollo.
## Si no los tienes instalados, puedes hacerlo con los siguientes comandos:
    pip install poetry
    poetry new myproject
    cd myproject
    poetry add typer

    sudo docker build -t my-typer-app .
    sudo docker run -d my-typer-app