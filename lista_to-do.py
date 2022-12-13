import sqlite3

connection = sqlite3.connect("todo.db")

def create_table(connection):
    try:
     cur = connection.cursor()
     cur.execute("""CREATE TABLE task (task text)""")
    except:
        pass 

def show_task(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()

    for row in result:
        print(str(row[0]) + " - " + row[1])

def add_lista(connection):
    lista = input("Wpisz treść zadania: ")
    if lista == "0":
        print("Powrtów do menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (lista,))
        connection.commit()
        print("Dodano zadanie.")

def delete_lista(connection):
    lista_index = int(input("Podaj index zadania, którego chcesz usunąć."))
    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""", (lista_index,)).rowcount
    connection.commit()
    
    if rows_deleted == 0:
        print("Takie zadanie nie istnieje.")
    else:
        print("Usunięto zadanie.")

create_table(connection)

while True:
    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdż")

    user1 = int(input("Wybierz liczbę: "))
    
    if user1 == 1:
       show_task(connection)

    if user1 == 2:
       add_lista(connection)
    
    if user1 == 3:
       delete_lista(connection)

    if user1 == 4:
        break
connection.close()