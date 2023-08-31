###############################################################################


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    return(max(a,b,c,d))
    """Re-escribir para que tome 4 parámetros, utilizar la función max.

    Referencia: https://docs.python.org/3/library/functions.html#max"""


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN