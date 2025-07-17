import telebot
from telebot import types
from utils import tipo_dolar, tipo_dato, start_msg

try:   #!! Recorda reemplazar el contenido por tu TOKEN en el archivo token.txt
    with open("token.txt", "r", encoding="utf-8") as f:   
        TOKEN = f.read()
        f.close()
except:
    print(" ⛔📄Archivo no encontrado o imposible de leer")
    
bot = telebot.TeleBot(TOKEN)


# Creamos el menú de opciones
def enviar_menu(chat_id, text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,is_persistent=True)
    btn1 = types.KeyboardButton("🏦 Oficial")
    btn2 = types.KeyboardButton("🔷 Blue")
    btn3 = types.KeyboardButton("💳 Tarjeta")
    btn4 = types.KeyboardButton("📚 Menú")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id, text, reply_markup=markup)
    




# Cuando recibe cualquier mensaje
@bot.message_handler(func=lambda message: True)
def manejar_mensaje(message):
    
    chat_id = message.chat.id
   
    if message.text == "/start" or message.text ==  tipo_dato[3]:
        enviar_menu(chat_id, start_msg)
        
    else:
        
        if message.text == tipo_dato[0]:  #! dolar oficial
                msg = tipo_dolar(tipoDeDolar = 'oficial')
                bot.reply_to(message, msg)
        elif message.text == tipo_dato[1]: #? dolar Blue
                msg = tipo_dolar(tipoDeDolar= 'blue')
                bot.reply_to(message, msg)
        elif message.text == tipo_dato[2]: # dolar Tarjeta
                msg = tipo_dolar(tipoDeDolar='tarjeta')
                bot.reply_to(message, msg)
        else:
            pass

        

bot.infinity_polling()

