#import tkinter as tk
#from PIL import ImageTk
import imageio
#import cv2

def display_gif(window, gif_path):
    # Загрузка GIF-изображения
    gif_image = Image.open(gif_path)

    # Создание последовательности кадров GIF
    frames = []
    for frame in range(0, gif_image.n_frames):
        gif_image.seek(frame)
        frames.append(ImageTk.PhotoImage(gif_image.copy()))

    # Создание виджета Label
    label = tk.Label(window)

    def update_label(frame):
        label.configure(image=frames[frame])
        window.after(5, update_label, (frame + 1) % len(frames))

    # Обновление изображения на Label
    update_label(0)

    # Упаковка виджета Label
    label.pack()



def display_gif_with_transparent_background(window, gif_path):
    # Удаление черного фона из кадров GIF
    frames_without_background = remove_black_background(gif_path)

    # Создание временных файлов с обработанными кадрами
    temp_filenames = []
    for i, frame in enumerate(frames_without_background):
        temp_filename = f"temp_frame_{i}.png"
        cv2.imwrite(temp_filename, frame)
        temp_filenames.append(temp_filename)

    # Создание анимации без фона с помощью imageio
    gif_without_background_path = "animation_without_background.gif"
    with imageio.get_writer(gif_without_background_path, mode='I') as writer:
        for filename in temp_filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    # Отображение анимации в Tkinter
    gif_image = ImageTk.PhotoImage(file=gif_without_background_path)

    label = tk.Label(window, image=gif_image)
    label.pack()

    window.mainloop()

    # Удаление временных файлов
    for filename in temp_filenames:
        os.remove(filename)

    # Удаление временного файла с анимацией без фона
    os.remove(gif_without_background_path)



#------------------------------------------------------------#
                         #SQL ЗАПОРОСХО
#------------------------------------------------------------#
    

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




def insert_data( idVal, familyaVal, imyaVal, otchestvoVal, doljnostVal):
    # Получение соединения с базой данных
    connection = connector()

    try:
        cursor = connection.cursor()
        sql_insert_query = "INSERT INTO employees (id, familya, imya, otchestvo, doljnost) VALUES (%s, %s, %s, %s, %s)"
        data = (idVal, familyaVal, imyaVal, otchestvoVal, doljnostVal)
        cursor.execute(sql_insert_query, data)
        connection.commit()
        print("Данные успешно добавлены в базу данных")
    except mysql.connector.Error as error:
        print(f"Ошибка при добавлении данных в базу данных: {error}")

    # Закрытие соединения с базой данных
    connection.close()

# Пример использования функции добавления данных
#insert_data('Makhkamov', 'Dilovar', 'Farhodjonovich', 'programmist', '4446465')


def delete_by_id(idVal):
    
    # Получение соединения с базой данных
    connection = connector()
    
    try:
        cursor = connection.cursor()
        sql_delete_query = "DELETE FROM employees WHERE id = %s"
        data = (idVal,)
        cursor.execute(sql_delete_query, data)
        connection.commit()
        print("Данные успешно удалены из базу данных")
    except mysql.connector.Error as error:
        print(f"Ошибка при удалении данных из базу данных: {error}")

    # Закрытие соединения с базой данных
    connection.close()

#delete_by_id(2)


def select():
    
    # Получение соединения с базой данных
    connection = connector()
    
    try:
        cursor = connection.cursor()
        sql_select_query = "SELECT * FROM employees"
        
        cursor.execute(sql_select_query)
        data = cursor.fetchall()

        # Извлечение 
        idVal = []
        familyaVal = []
        imyaVal = []
        otchestvoVal = []
        doljnostVal = []


        for row in data:
            id, familya, imya, otchestvo, doljnost = row
            idVal.append(id)
            familyaVal.append(familya)
            imyaVal.append(imya)
            otchestvoVal.append(otchestvo)
            doljnostVal.append(doljnost)

        print("Данные успешно получены из базы данных")
        return idVal, familyaVal, imyaVal, otchestvoVal, doljnostVal

    except mysql.connector.Error as error:
        print(f"Ошибка при получении данных из базы данных: {error}")

    # Закрытие соединения с базой данных
    connection.close()

# Пример использования функции и сохранение данных в переменные
#D = select()
#print(D)


def select_name_byid(idValue):
    
    # Получение соединения с базой данных
    connection = connector()
    
    try:
        cursor = connection.cursor()
        sql_select_query = "SELECT * FROM employees where id = %s"
        id = (idValue,)
        cursor.execute(sql_select_query, id)
        data = cursor.fetchall()

        # Извлечение 
        idVal = ""
        familyaVal = ""
        imyaVal = ""
        otchestvoVal = ""
        doljnostVal = ""
        parolVal = ""

        for row in data:
            id, familya, imya, otchestvo, doljnost = row
            idVal = id
            familyaVal = familya
            imyaVal = imya
            otchestvoVal = otchestvo
            doljnostVal = doljnost

        print("Данные успешно получены из базы данных")
        return idVal, familyaVal, imyaVal, otchestvoVal, doljnostVal

    except mysql.connector.Error as error:
        print(f"Ошибка при получении данных из базы данных: {error}")

    # Закрытие соединения с базой данных
    connection.close()
    
#print(select_name_byid(4))




def select_id():
    
    # Получение соединения с базой данных
    connection = connector()
    
    try:
        cursor = connection.cursor()
        sql_select_query = "SELECT id FROM employees"
        cursor.execute(sql_select_query)
        data = cursor.fetchall()

        # Извлечение 
        idVal = []

        for row in data:
            id = row
            idVal = id

        print("Данные успешно получены из базы данных")
        return idVal

    except mysql.connector.Error as error:
        print(f"Ошибка при получении данных из базы данных: {error}")

    # Закрытие соединения с базой данных
    connection.close()


#------------------------------------------------------------#
                         #
#------------------------------------------------------------#


def proverkaID(idVal):

    data = select_id()
    
    bl = (idVal in data)

    return bl
    
#print(proverkaID("4444"))






                         

