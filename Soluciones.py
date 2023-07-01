def custon_max(n1: int, n2: int):
    """Dados dos numeros de entrada, retornar el mayor

    Args:
        n1 (int): primer numero a comparar
        n2 (int): segundo numero a comparar


        returns:
            int: Mayor de ambos

    """

    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    raise Exception("Algo salio mal")

print(custon_max(3,2))