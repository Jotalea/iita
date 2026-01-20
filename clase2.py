# actividad 1
def descuento(precio:float, porcentaje:int):
    """esta función toma un precio y le aplica un descuento"""
    return precio - ( precio * ( porcentaje / 100 ) )

# actividad 2
def convertir_temperatura(temperatura:int, medida:str, objetivo:str):
    def convertir_temperatura(temperatura: int, medida: str, objetivo: str):
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
        return float(truncate(temperatura * 1.8 + 32, 2))
    elif medida.lower() in fahrenheit and objetivo.lower() in celsius:
        return float(truncate(( temperatura - 32 ) / 1.8, 2))
    else:
        return "inválido"
