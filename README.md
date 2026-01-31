API Universidades

Proyecto desarrollado en Python utilizando FastAPI, basado en la estructura vista en clase para el consumo de APIs externas.
La API permite consultar universidades por país, consumiendo información desde una API pública y devolviendo una respuesta estructurada.

API externa utilizada

Universities API – Hipolabs

URL base: http://universities.hipolabs.com

Formato: JSON

Autenticación: No requerida

Tipo: API pública

Esta API retorna información de universidades a nivel mundial filtradas por país.

Endpoint implementado
Obtener universidades por país

URL

/universities/{country}


Método

GET


Parámetros

Nombre	             Tipo	                              Descripción
country	             string	                              Nombre del país a consultar


Ejemplo de petición

GET /universities/colombia

Respuesta exitosa

Código
200 OK


Ejemplo de respuesta

{
  "country": "colombia",
  "total": 2,
  "universities": [
    {
      "name": "Universidad Nacional de Colombia",
      "website": "http://www.unal.edu.co/",
      "domains": ["unal.edu.co"]
    },
    {
      "name": "Universidad de los Andes",
      "website": "https://uniandes.edu.co/",
      "domains": ["uniandes.edu.co"]
    }
  ]
}

Campos en la respuesta

Campo	                          Tipo	                             Descripción
name	                          string	                         Nombre de la universidad
country	                          string	                         País donde está ubicada
domains	                          array	                             Lista de dominios del sitio web
web_pages	                      array	                             URLs públicas de la universidad


Manejo de errores comunes

Aunque esta API pública es simple, podrían darse algunos errores comunes:

Código HTTP	                     Significado	              Causa frecuente
400	                             Bad Request	              Parámetro inválido o faltante
404	                             Not Found	                  No hay universidades para el país consultado
500	                             Server Error	              Error interno del servicio


Manejo de errores
Error consultando la API externa

Código

500 Internal Server Error


Ejemplo

{
  "detail": "Error consultando la API de universidades"
}


Este error se presenta cuando la API externa no responde o ocurre un problema en la comunicación.

Tecnologías utilizadas

Python 3

FastAPI

Uvicorn

HTTPX



Ejecución del proyecto

Activar entorno virtual:

.\venv\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

uvicorn main:app --reload


Acceder a la documentación:

http://127.0.0.1:8000/docs



Estructura del proyecto
api_universidades/
├── clients
├── controllers
├── services
├── DTOs
├── main.py
├── appsettings.py
├── requirements.txt
└── README.md



Observación
El proyecto reutiliza la estructura base trabajada en clase, adaptándola para el consumo de una nueva API pública, cumpliendo con los lineamientos del taller práctico.