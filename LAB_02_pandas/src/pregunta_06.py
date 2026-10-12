import pandas as pd
from pathlib import Path

# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / "data"
ARCH_DATOS = DIR_DATOS / "tbl1.tsv"

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_06():
    """
    Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
    conviértalos a mayúsculas y retórnelos como una lista ordenada
    alfabéticamente.

    Ejemplo del formato de la respuesta:

        ["A", "B", "C", "D", "E", "F", "G"]
    """
    
    df = pd.read_csv(ARCH_DATOS, sep= "\t")
    grupos = df["c4"].str.upper().unique()
    return(sorted(grupos))

print(pregunta_06())



