import pandas as pd
from pathlib import Path


# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / 'data'
ARCH_DATOS = DIR_DATOS / 'data.csv.gz'

# Existencia de dicha ruta
assert ARCH_DATOS.exists()

def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """
    df = pd.read_csv(ARCH_DATOS, sep="\t", header=None)
    meses = df[2].str.split("-").str[1]                        # 2. Extraer el mes de la tercera columna (índice 2)
    counts = meses.value_counts().sort_index()                 # 3. Contar la frecuencia de cada mes y ordenar por la clave (mes)
    return list(counts.items())                                # 4. Convertir a lista de tuplas

print(pregunta_04())
