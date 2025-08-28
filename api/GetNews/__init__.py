import azure.functions as func
import os
import requests
import json

async def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Leer API Key desde Application Settings
        api_key = os.environ["NEWSAPI_KEY"]

        # Leer parámetros desde la query (con valores por defecto)
        country = req.params.get("country", "us")
        category = req.params.get("category", "technology")

        # URL de NewsAPI
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": country,
            "category": category,
            "apiKey": api_key
        }

        # Hacer la request a NewsAPI
        response = requests.get(url, params=params)
        data = response.json()

        # Extraer solo titulares
        headlines = [{"title": article["title"]} for article in data.get("articles", [])]

        return func.HttpResponse(
            json.dumps(headlines, ensure_ascii=False, indent=2),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
