from functools import reduce

def partir(linea):
    return linea.split(" ")

dir_base = "text/disc_"
contenido = []
for i in range(0,774):
    with open(dir_base + str(i) + ".txt") as f:
        contenido = contenido + f.readlines()

print("Parrafos: " + str(len(contenido)))

contenido = [x.strip() for x in contenido]

contenido = map(partir, contenido)

contenido = reduce(lambda a, b: a + b, contenido)

print(contenido)
