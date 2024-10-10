print(" ")
print("Arzaba Diaz April 3W 1173")
def longitud_ultima_palabra(cadena):
    """
    Esta funcion devuelve la longitud de la ultima palabra en un string.
    Las palabras estan separadas por uno o mas espacios. #en esta linea
    
    Args:
    cadena (str): La cadena de texto de entrada.

    Returns:
    int: La longitud de la ultima palabra. Si no hay palabras, devuelve 0.
    """
    # Eliminamos espacios al inicio y al final, y luego dividimos la cadena por espacios
    palabras = cadena.strip().split()
    
    # Verificamos si hay palabras en la lista
    if palabras:
        # Devolvemos la longitud de la ultima palabra
        return len(palabras[-1])
    else:
        # Si no hay palabras, devolvemos 0
        return 0

# Ejemplo de uso
resultado = longitud_ultima_palabra("   hola mundo   ")
print(resultado)  # Salida: 5
