#Versión simple del algoritmo
# Pensada para desarrollar rápido, sin importar eficiencia ni consumo de recursos.
def suma_simple(nums, requiredSum):
    # Recorremos todos los pares posibles del array
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == requiredSum:
                return True
    return False


#Versión eficiente del algoritmo
#Pensada para optimizar tiempo de ejecución.
def suma_eficiente(nums, requiredSum):
    vistos = set()  # Usamos un set para buscar complementos en tiempo constante
    for num in nums:
        complemento = requiredSum - num
        if complemento in vistos:
            return True
        vistos.add(num)
    return False


