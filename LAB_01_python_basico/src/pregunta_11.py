import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"a": 122, "b": 49, "c": 91, ...}
    """
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    df[3] = df[3].str.split(",")
    df_exploded = df.explode(3)
    suma_por_letra = df_exploded.groupby(3)[1].sum().sort_index()
    return dict(suma_por_letra)
    

print(pregunta_11())
