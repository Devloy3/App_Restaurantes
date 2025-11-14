import sqlite3

conn = sqlite3.connect("../db/restaurantes.db")
cursor = conn.cursor()

localizaciones = [
                (41.4147909,2.1645314,1), 
                (41.4148043,2.1648082,2),
                (41.4292744,2.1624673,3),
                (41.8448761,2.2398402,4),
                (41.4559968,2.2272397,5),
]

for latitud,longitud,id in localizaciones:
    cursor.execute("INSERT INTO localizaciones(latitud,longitud,id_restaurante) VALUES (?,?,?)", (latitud,longitud,id))

conn.commit()