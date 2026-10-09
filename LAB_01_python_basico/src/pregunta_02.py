def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """
    df = pd.read_csv("data/data.csv.gz", sep="\t", header=None)
    counts = df[0].value_counts().sort_index()
    return list(counts.items())

      
