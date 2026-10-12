import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """
    
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    pares = df[4].str.split(",")
    filas = pares.explode()
    Clave_Valor = filas.str.split(":", expand=True)
    Clave_Valor[1] = Clave_Valor[1].astype(int)
    Salida = Clave_Valor.groupby(0)[1].agg(["min", "max"]).sort_index()
    return(list(zip(Salida.index, Salida["min"], Salida["max"])))
    

print(pregunta_06())






