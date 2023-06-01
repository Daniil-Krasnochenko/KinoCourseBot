import sqlite3
import config
def find_genres(country):
     # Поиск рекомендаций в базе данных
    conn = sqlite3.connect(config.db.database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM country='{country}'  ORDER BY RAND() LIMIT 5")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    
    return results

def find_actor(actors):

    conn = sqlite3.connect(config.db.database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM actor='{actors}'  ORDER BY RAND() LIMIT 5")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    
    return results


def find_genres(genres):
     # Поиск рекомендаций в базе данных
    conn = sqlite3.connect(config.db.database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM genre='{genres}'  ORDER BY RAND() LIMIT 5")
    results = cursor.fetchall()
    conn.commit()
    conn.close()

    return results