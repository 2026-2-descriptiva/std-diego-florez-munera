import pandas as pd
from pathlib import Path
import re

# Rutas
DIR_DATOS = Path(__file__).resolve().parent.parent / "data"
ARCH_DATOS = DIR_DATOS / "clusters_report.txt"

# Existencia de dicha ruta
assert ARCH_DATOS.exists()


def pregunta_01():
    """
    El archivo `data/clusters_report.txt` es un reporte de clústeres de
    palabras clave pensado para ser leído por una persona, no por un programa:
    los encabezados ocupan varias líneas, las columnas están alineadas con
    espacios y la lista de palabras clave de un clúster continúa en las líneas
    siguientes.

    Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
    por clúster y las columnas:

    - `cluster`: número del clúster, como entero.
    - `cantidad_de_palabras_clave`: como entero.
    - `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
      texto `15,9 %` debe quedar como `15.9`.
    - `principales_palabras_clave`: todas las palabras clave del clúster en un
      solo texto, separadas por una coma y un único espacio.

    Retorne el DataFrame.

    Ejemplo del formato de la respuesta (se omite la última columna):

           cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
        0        1                         105                          15.9
        1        2                         102                          15.4
        ...
    """
    
    contenido = ARCH_DATOS.read_text(encoding="utf-8")
    
    patron = r"^\s*(\d+)\s+(\d+)\s+(\d+,\d+)\s*%\s*(.*?)(?=\n\s*\d+\s+\d+|\Z)"
    coincidencias = re.findall(patron, contenido, flags=re.MULTILINE | re.DOTALL)
    
    df = pd.DataFrame(
        coincidencias,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )
    
    df["cluster"] = df["cluster"].astype(int)
    df["cantidad_de_palabras_clave"] = df[
        "cantidad_de_palabras_clave"
    ].astype(int)
    df["porcentaje_de_palabras_clave"] = (
        df["porcentaje_de_palabras_clave"].str.replace(",", ".").astype(float)
    )

    # 5. Limpieza vectorizada del texto de palabras clave
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(
            r"\s+", " ", regex=True
        )  # Remplaza saltos de línea (\n) y múltiples espacios por 1 espacio
        .str.replace(
            r"\s*,\s*", ", ", regex=True
        )  # Estandariza comas: quita espacios antes y deja 1 después
        .str.replace(r"\.\s*$", "", regex=True)  # Elimina el punto final
        .str.strip()
    )
    
    return(df)
  
  
print(pregunta_01())

