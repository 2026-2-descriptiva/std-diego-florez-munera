import pandas as pd

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """

    df = pd.read_csv("data/data.csv.gz", sep="\t", header=None)
    return print(int(df[1].sum()))