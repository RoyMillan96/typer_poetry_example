import typer
import requests
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Crea la aplicación Typer
app = typer.Typer()

# Configura la conexión a la base de datos con SQLAlchemy
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/db_salinas"
engine = create_engine(DATABASE_URL)

# Define un modelo utilizando SQLAlchemy
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Crea la tabla en la base de datos (solo una vez)
Base.metadata.create_all(bind=engine)

# Crea una función para obtener una sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.command()
def fetch_data(name_city: str):
    # URL del endpoint externo que deseas consultar
    api_key = os.getenv("apikey") if os.getenv("apikey") else 'kxiSQEbqAlvHjVWA8NRVbpXUGfilvuGq'
    url = 'http://dataservice.accuweather.com/locations/v1/cities/search'

    params = {
            'q': name_city,
            'apikey': api_key
        }
    try:
        # Realiza la solicitud GET al endpoint
        response = requests.get(url, params=params)

        # Verifica si la solicitud fue exitosa (código de estado HTTP 200)
        if response.ok:
            data = response.json()
            print("la data es: ", data)
        else:
            print(f'La solicitud no fue exitosa. Código de estado: {response.status_code}')
    except Exception as error:
        print(f'La solicitud no fue exitosa. Código de estado: 500')


if __name__ == "__main__":
    app()