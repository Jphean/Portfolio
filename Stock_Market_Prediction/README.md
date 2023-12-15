# Proyecto: Pedicción de precios de acciones de la bolsa de NY
## Descripción:
Esta aplicación realiza una predicción gráfica de los precios, de los siguientes 2 meses, de las acciones.
Solo se requiere de un input, el ticker de la acción. El ticker es el nombre que representa la acción de una empresa.
Se ha construido esta aplicación en base al lenguaje Python por la siguiente razón; Python provee una amplia
gama de librerías para realizar modelos predictivos con facilidad.
El proceso de desarrollo del proyecto consta de los siguientes pasos:
* Recolección de datos: Se obtienen los datos mediante la librería _yfinance_.
* Preparación de los datos: Separación de la data de entrenamiento y prueba.
* Elección del modelo: El modelo que se elige es de redes neuronales recurrentes.
* Evaluación del modelo: Mediante el gráfico se analiza el grado de precisión del modelo.
* Implementación: Se implementa en una aplicación para que el usuario pueda analizar fácilmente las acciones.
## Lenguajes y herramientas:
* Python
* Visual studio Code
* Pandas
* Numpy
* Keras
* Scikit-Learn
## Instrucciones:
Instala las siguientes librerías<br>
```pip install pandas numpy tensorflow Tk sklearn yfinance plotly.express pandas_market_calendars matplotlib ```<br><br>
Luego ejecuta el archivo ```stock_market_prediction.py``` 
La interfaz solicita el nombre de un ticker por ejemplo:
* AAPL
* MFST
* AMZN
## Créditos:
Este proyecto fue desarrollado en colaboración de:
* Renzo
* Bernabe
* Eduardo
* Johana
* Gladys

