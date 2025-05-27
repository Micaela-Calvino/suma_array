from suma import suma_simple, suma_eficiente # type: ignore

def test():
    assert suma_simple([1, 4, 3, 9], 8) == False
    assert suma_simple([1, 2, 4, 4], 8) == True
    assert suma_simple([-1, -3, -5, -7], -4) == True
    assert suma_eficiente([1, 4, 3, 9], 8) == False
    assert suma_eficiente([1, 2, 4, 4], 8) == True
    assert suma_eficiente([-1, -3, -5, -7], -4) == True
    print("Todos los tests pasaron correctamente.")

test()
