import typer
import os
import requests
from typing import Optional
from typing_extensions import Annotated

# Crea la aplicación Typer
app = typer.Typer()

@app.command()
# manda parametros opcionales 
def fetch_data(name_city: Annotated[Optional[str], typer.Argument()] = None):
    # URL del endpoint externo que deseas consultar
    api_key = os.getenv("apikey") if os.getenv("apikey") else 'kxiSQEbqAlvHjVWA8NRVbpXUGfilvuGq'
    url = 'http://dataservice.accuweather.com/locations/v1/cities/search'

    params = {
            'q': name_city if name_city else 'Toluca',
            'apikey': api_key
        }
    print('request: ', params)
    try:
        # Realiza la solicitud GET al endpoint
        response = requests.get(url, params=params)

        # Verifica si la solicitud fue exitosa (código de estado HTTP 200)
        if response.ok:
            data = response.json()
            # print("la data es: ", data)
        else:
            print(f'La solicitud no fue exitosa. Código de estado: {response.status_code}')
    except Exception as error:
        print(f'La solicitud no fue exitosa. Código de estado: 500')

if __name__ == "__main__":
    app()