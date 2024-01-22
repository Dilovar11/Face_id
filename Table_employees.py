import pandas as pd
import tkinter as tk
from tkinter import ttk
import mysql.connector

def connector(): 
    # Установка соединения с базой данных
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="face_recognition"
    )
    return connection


def select_data_by_date():
    # Подключение к базе данных
    connection = connector()

    # Выбор данных из базы данных по выбранной дате
    #query = "SELECT id, familya, imya, otchestvo, doljnost, date, time, status FROM combined_status WHERE date = '{selected_date}'"
    cursor = connection.cursor()
    sql_select_query = "SELECT * FROM combined_status"
    cursor.execute(sql_select_query,)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)
    connection.close()


# Создание графического интерфейса    
root = tk.Tk()
root.geometry("1280x720")
root.title("БД СОТРУДНИКОВ")

                   
tree_columns = ['ID', 'ФАМИЛИЯ', 'ИМЯ', 'ОТЧЕСТВО', 'ДОЛЖНОСТЬ', 'ДАТА', 'ВРЕМЯ', 'СТАТУС']
tree = ttk.Treeview(root, columns=tree_columns, show="headings")
for column in tree_columns:
    tree.heading(column, text=column)
    tree.column(column, anchor="center")
tree.pack(fill="both", expand=True)
                   

select_data_by_date()

# Создание полосы прокрутки
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)




root.mainloop()
