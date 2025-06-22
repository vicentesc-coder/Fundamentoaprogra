def menu():
    print('*** MENU PRINCIPAL ***')
    print('1.- Turistas por país.')
    print('2.- Turista por mes.')
    print('3.- Eliminar turista.')
    print('4.- Salir')

def turistas_por_pais(diccionario):
    paisturista = input('Ingrese pais: ')
    lista = []
    for clave in diccionario.values():
        if clave[1].upper() == paisturista.upper():
            lista.append(clave[0])
    print(lista[:])

def turistas_por_mes(diccionario):
    contador = 0
    mes = input('Ingrese mes con numero: ')
    if len(mes) == 1:
        mes = '0' + mes
    total = len(diccionario)
    for clave in diccionario.values():
        fecha = clave[2]
        i = fecha[3:5]
        if i == mes:
            contador += 1
    porcentaje = 100*contador/total
    print(f'El porcentaje de los turistas que vienen en {mes} es de %',round(porcentaje,1))

def eliminar_turista(diccionario):
    nombre = input('Ingrese nombre del turista a eliminar: ')
    for clave in diccionario:
        if diccionario[clave][0] == nombre:
            del diccionario[clave]
            print('Turista eliminado con exito')
            return diccionario
    else:
        print('Turista no encontrado')
    return diccionario

