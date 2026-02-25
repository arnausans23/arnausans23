def calcular_total_ingresos(df):
    """Devuelve el total de ingresos redondeado a 2 decimales."""
    total = round(df["price"].sum(), 2)
    return total
