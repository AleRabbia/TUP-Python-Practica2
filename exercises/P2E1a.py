"""Bloque IF, operadores lógicos, función max y operador ternario."""


def maximo_basico(a: float, b: float) -> float:
    if (a > b):
        print(a)
        return a
    print(b)
    return b
    
    
    """Toma dos números y devuelve el mayor.

    
    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
    """


# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN

