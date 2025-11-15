from db.db import Relacional

prueba = Relacional()

promedio_total = prueba.promedio_total()
promedio_rest = prueba.promedio_restaurante()
restaurantes = prueba.mostrar_restaurantes()



print(restaurantes)