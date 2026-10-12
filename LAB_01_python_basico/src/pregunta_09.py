import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    pares = df[4].str.split(",")
    filas = pares.explode()
    Clave_Valor = filas.str.split(":", expand=True)
    Conteo = Clave_Valor[0].value_counts().sort_index()
    return(dict(Conteo))
    
    
print(pregunta_09())
   


