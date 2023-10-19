import typer
import os
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Crea la aplicación Typer
app = typer.Typer()

# Configura la conexión a la base de datos con SQLAlchemy
# DATABASE_URL = "postgresql://postgres:1234@localhost:5432/db_salinas"
# engine = create_engine(DATABASE_URL)

# Crea una función para obtener una sesión de SQLAlchemy
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.command()
def service_cleaner(variable_entorno: str = os.getenv("apikey")):
    typer.echo(f"El valor de la variable de entorno es: {variable_entorno}")

if __name__ == "__main__":
    app()