from typing import Union

def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501

    if multiplicar: 
        return a*b
    
    if b!= 0: 
        return a/b

    return "Operación no válida"
        

    
    """Re-Escribir el ejercicio anterior utilizando tres returns.

    
    Restricciones:
        - Utilizar 2 IF.
        - No Utilizar IF anidados.
        - No utilizar ELIF ni ELSE.
        - No utilizar AND ni OR.
    """


# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN
