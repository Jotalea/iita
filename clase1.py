# actividad 1
def a(b:list):
    s = set(b.sort())
    return s

# actividad 2
esto_es_un_set = set()
while True:
    print(sorted(list(esto_es_un_set)))
    prompt = input("[s]alir, [a]gregar o [e]liminar un valor? ").lower()
    if prompt.startswith("s"):
        break
    if prompt.startswith("a") or prompt.startswith("e"):
        accion = "agregar" if prompt.startswith("a") else "eliminar"
        valor = input(f"decime el valor a {accion}: ")

        if prompt.startswith("a"):
            esto_es_un_set.add(valor)
        else:
            esto_es_un_set.discard(valor)
    else:
        print("y eso?")

# actividad 3
s1 = {3,6,9}
s2 = {2,4,6}
print(s1 - s2)

# actividad 4
print(s1 | s2)

# actividad 5
def fact(num:float):
    # saqué la lógica de https://www.programiz.com/python-programming/examples/factorial
    if n < 0: return None
    r = 1
    for i in range(1, n + 1):
        r *= i
    return result

# actividad 6
def fibonacci(n:int):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)

# actividad 7
def suma_recursiva(num:float):
    c = num
    r = 0
    while c > 0:
        r = r + c
        c-=1
    return r

# actividad 8
class Libro:
    def __init__(self, titulo:str, autor:str, año_publicación:int):
        self.titulo = titulo
        self.autor = autor
        self.año_publicación = año_publicación

class LibroDigital(Libro):
    def __init__(self, titulo:str, autor:str, año_publicacion:int, puntaje:float):
        super().__init__(titulo, autor, año_publicacion)
        self.puntaje = puntaje

# actividad 9
def slicing_function(text:str):
    r = []
    for i in text.split("|"):
        for n in i.split(":"):
            r.append(n.strip())
    return dict(zip(r[::2], r[1::2]))

text = "Nombre: Juan Pérez | Edad: 30 | Ciudad: Salta"
slicing_function(text) # {"nombre": "Juan Perez", "edad"  30, "ciudad": "Salta"}
