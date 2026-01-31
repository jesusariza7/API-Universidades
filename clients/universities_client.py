import httpx

BASE_URL = "http://universities.hipolabs.com/search"


def fetch_universities(country: str):
    response = httpx.get(BASE_URL, params={"country": country})

    if response.status_code != 200:
        raise Exception("Error en la API externa")

    return response.json()
