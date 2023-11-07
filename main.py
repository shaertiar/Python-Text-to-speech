import tkinter as tk
import gtts
import os

# Количество генераций
generations = 0

# Функция генерации текста в звук
def generate_voice():
    global generations

    # Проверка на наличие папки
    try:
        os.mkdir('Voices')
    except:
        None

    # Текст
    entry_text = entry.get('1.0', "end-1c")

    if entry.get('1.0', "end-1c") != '':
        if language.get() != 'None':
            text['text'] = ''

            try:
                gtts.gTTS(entry_text, lang=language.get()).save('Voices/voice.mp3')
                text['text'] = f'Приобразование готово!\nФайл: Voices/voice.mp3 {"" if generations == 0 else f"(Обновлено {generations})"}'
                generations += 1
            except:
                text['text'] = 'Ошибка образованя.\nВы можете обратиться в тех. поддержку с подробным указанием проблемы: KAAOS.tgbot@gmail.com'
        else:
            text['text'] = 'Пожалуйста выберите язык!'
    else:
        text['text'] = 'Пожалуйста введите текст!'

# Создание окна
root = tk.Tk()
root.geometry('854x480')
root.title('Преобразователь текста в голос')
root.resizable(False, False)

# Создание бортька
frame = tk.LabelFrame(root, padx=20, pady=20)

# Создание текста 
text = tk.Label(frame, text='\n')

# Создание поля для ввода
entry = tk.Text(frame, width=99, height=17)

# Создание кнопки
button_start = tk.Button(frame, text='Преобразовать', command=generate_voice)

language = tk.StringVar()
language.set('None')

button_Ru = tk.Radiobutton(frame, text='Ru', variable=language, value='ru')
button_En = tk.Radiobutton(frame, text='En', variable=language, value='en')

# Размещение элеменотов
frame.pack(padx=5, pady=10)
entry.pack()
button_start.pack()
button_Ru.pack()
button_En.pack()
text.pack()
tk.Label(root, text='KAAOS from Shaertiar').pack()

# Запуск приложения
root.mainloop()