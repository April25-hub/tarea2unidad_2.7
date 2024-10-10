# tarea2unidad_2.7
Arzaba Diaz April 1173 3W
print(" ")
print("Arzaba Diaz April 3W 1173")
def longitud_ultima_palabra(cadena):
    """
    Esta función recibe una cadena de texto y devuelve la longitud de la última palabra.
    
    args:
    cadena (str): La cadena de texto de entrada.

    returns:
    int: la longitud de la última palabra en la cadena si no hay palabras, devuelve 0.
    """
    # esta linea eliminara espacios al inicio y al final, y luego dividimos la cadena por espacios
    palabras = cadena.strip().split()
    
    #esta linea verificara si hay palabras en la lista
    if palabras:
        #esta linea ara que se devuelva  la longitud de la última palabra
        return len(palabras[-1])
    else:
        #esta linea dira que si no hay palabras, devolvemos 0
        return 0

#esta linea dara un ejemplo  de uso
resultado = longitud_ultima_palabra("   hola mundo   ")
print(resultado)  #salida: 5
![image](https://github.com/user-attachments/assets/254e04b9-26b9-4ea8-ab98-011e1ed64d44)

