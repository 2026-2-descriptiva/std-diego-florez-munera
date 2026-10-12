import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """
    
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    df[4] = df[4].str.split(",")
    df_exploded = df.explode(4)
    df_exploded["val"] = df_exploded[4].str.split(":").str[1].astype(int)
    res = df_exploded.groupby(0)["val"].sum().sort_index()
    return dict(res)

print(pregunta_12())



