# actividad 1
def descuento(precio:float, porcentaje:int) -> float:
    """
    Calcula el precio final de un producto aplicando un descuento.

    Args:
        precio (float): El precio original del producto.
        porcentaje (int): El porcentaje de descuento a aplicar (0-100).

    Returns:
        float: El precio final tras aplicar el descuento.
    """
    return float(precio - (precio * (porcentaje / 100)))

# actividad 2
def convertir_temperatura(temperatura:int, medida:str, objetivo:str) -> str:
    """
    Convierte un valor de temperatura entre Celsius y Fahrenheit.

    Toma un valor numérico y traduce su escala basándose en las unidades
    de origen y destino proporcionadas. Soporta múltiples sinónimos para 
    las unidades (ej: 'c', 'Celsius', 'f', 'Fahrenheit').

    Args:
        temperatura (int/float): El valor numérico a convertir.
        medida (str): La unidad original ('c' o 'f').
        objetivo (str): La unidad a la que se desea convertir ('c' o 'f').

    Returns:
        float: El resultado de la conversión redondeado a 2 decimales.
        None: Si una de las unidades no es reconocida.

    Examples:
        >>> convertir_temperatura(37, "c", "f")
        98.6
        >>> convertir_temperatura(78, "f", "c")
        25.56
    """
    
    fahrenheit = ["f", "°f", "fahrenheit", "grados fahrenheit", "grados f"]
    celsius = ["c", "°c", "celsius", "centigrados", "centígrados", "grados centígrados", "grados centigrados", "grados celsius", "grados c"]
    
    if medida.lower() in celsius and objetivo.lower() in celsius or medida.lower() in fahrenheit and objetivo.lower() in fahrenheit:
        return temperatura

    def truncate(f, n):
        # Source - https://stackoverflow.com/questions/783897/how-to-truncate-float-values
        # Posted by David Z, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-01-20, License - CC BY-SA 3.0

        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d+'0'*n)[:n]])

    
    if medida.lower() in celsius and objetivo.lower() in fahrenheit:
        return str(float(truncate(temperatura * 1.8 + 32, 2)))
    elif medida.lower() in fahrenheit and objetivo.lower() in celsius:
        return str(float(truncate(( temperatura - 32 ) / 1.8, 2)))
    else:
        return "inválido"

# Actividad 3
def es_palindromo(texto:str) -> bool:
    texto_array = []
    for caracter in texto:
        texto_array.append(caracter)
    if texto_array == texto_array.reverse():
        return True
    return False
    
# actividad 4
def info_texto(texto:str) -> str:
    """
    Cuenta la cantidad de palabras y caracteres en un texto.

    Args:
        texto (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario con el siguiente formato:
              {'palabras': int, 'caracteres': int}
    """
    palabras_total = 0
    caracteres_total = 0
    for palabra in texto.split():
        palabras_total += 1
    for caracter in texto:
        caracteres_total += 1
    return f"el texto contiene {palabras_total} palabras, y {caracteres_total} caracteres"

# actividad 5
def generar_primos(limite: int) -> list:
    """
    Genera una lista de números primos hasta un número dado.

    Un número primo es un número natural mayor que 1 que tiene 
    únicamente dos divisores distintos: él mismo y el 1.

    Args:
        limite (int): El número entero positivo hasta donde buscar.

    Returns:
        list: Lista de enteros primos encontrados.
    """
    numeros_primos = []
    for numero in range(2, limite + 1):
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(numero)
    return numeros_primos
    
# actividad 6
def actualizar_inventario(inventario: dict, vendidos: list) -> dict:
    """
    Actualiza las cantidades del inventario restando los productos vendidos.

    Args:
        inventario (dict): Diccionario {producto: cantidad}.
        vendidos (list): Lista de nombres de productos vendidos.

    Returns:
        dict: El inventario actualizado.

    Example:
        >>> actualizar_inventario({"manzanas": 10}, ["manzanas", "manzanas"])
        {"manzanas": 8}
    """
    for producto in vendidos:
        if producto in inventario:
            inventario[producto] -= 1
    return inventario

# actividad 7
