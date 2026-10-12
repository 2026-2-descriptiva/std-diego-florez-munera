import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    SumaOrdenada = df.groupby(0)[1].sum().sort_index()
    return(list(SumaOrdenada.items()))

    
print(pregunta_03())