import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """
    
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    MaxMin = df.groupby(0)[1].agg(["max", "min"]).sort_index()
    return list(zip(MaxMin.index, MaxMin["max"], MaxMin["min"]))
    
    
print(pregunta_05())
    


    



