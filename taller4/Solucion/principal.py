import funciones as fc
turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "50-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

opc = ''
while opc != '4':
    fc.menu()
    opc = input('---->')
    if opc == '1':
        fc.turistas_por_pais(turistas)
    elif opc == '2':
        fc.turistas_por_mes(turistas)
    elif opc == '3':
        fc.eliminar_turista(turistas)
    elif opc == '4':
        print('Salir')
    else:
        print('Opción no válida.')