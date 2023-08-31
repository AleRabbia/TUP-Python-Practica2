###############################################################################


def maximo_ternario(a: float, b: float) -> float:

    return a if (a > b) else b
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """


# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
