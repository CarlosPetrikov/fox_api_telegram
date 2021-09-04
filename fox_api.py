import requests
import telebot
import random
from time import sleep, time

#👇 PUT YOUR BOT TOKEN HERE 👇
token = ''
bot = telebot.TeleBot(token)

fox_dict = {
1: 'A little fox to liven up your day 🦊',
2: 'Another day, another fox 🦊',
3: 'Who gets tired of cute foxes, huh? 🦊',
4: "I don't have many catchphrases, but the important thing is the foxes, right? 🦊",
5: 'Foxes and more foxes, welcome to the paradise 🦊',
6: 'What does the fox say? 🎶 🦊',
7: "I can't think in a cool phrase right now... But here's one more fox 🦊",
8: "Wait stranger, don't go alone... Leave this cute fox with you 🥺🦊"
}


# dictionary to map users steps
user_dict = {}
# dictionary to map user current timestamp in each step
id_timestamp = {}

# object of the class User, created with base on user chat id
class User:
    def __init__(self, id):
        self.id = id
        self.temp = None
        self.keyboard = None
        

# function to receive any message and reply with the selection menu
@bot.message_handler(func=lambda m: True)
def inicio(message):
    # to not reply multiple messages with the same menu:
    # if the user not in id_timestamp dictionary 
    # or the difference between current timestamp and timestamp in the dictionary is greather than 5s,
    # then chatbot will reply the user.
    if message.chat.id not in id_timestamp or (time() - id_timestamp[message.chat.id]) > 5:
        user = User(message.chat.id) 
        user_dict[message.chat.id] = user
        id_timestamp[message.chat.id] = time()
        
        response = requests.get('https://randomfox.ca/floof/')
        fox = response.json()
        
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, fox_dict[random.randrange(1,9)])
        bot.send_photo(message.chat.id, fox['image'])
        
        user.keyboard = telebot.types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True, one_time_keyboard=True)
        user.keyboard.add("Of course! You think I'm crazy??? ❤️", "Nah... I hate foxes and I don't have a heart 💩🔫🦊")
        
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.send_message(message.chat.id, 'Sooo... Another fox? 🥺🥺🥺', reply_markup=user.keyboard) 
        
        bot.register_next_step_handler(msg, choose_step)
        
def choose_step(message):
    user = user_dict[message.chat.id]
    user.temp = message.text
    
    if user.temp == "Of course! You think I'm crazy??? ❤️":
        response = requests.get('https://randomfox.ca/floof/')
        fox = response.json()
        
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, fox_dict[random.randrange(1,9)])
        bot.send_photo(message.chat.id, fox['image'])
        
        user.keyboard = telebot.types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True, one_time_keyboard=True)
        user.keyboard.add("Of course! You think I'm crazy??? ❤️", "Nah... I hate foxes and I don't have a heart 💩🔫🦊")
        
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.send_message(message.chat.id, 'Sooo... Another fox? 🥺🥺🥺', reply_markup=user.keyboard) 
        
        bot.register_next_step_handler(msg, choose_step)
    
    elif user.temp == "Nah... I hate foxes and I don't have a heart 💩🔫🦊":
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, 'Hahaha... Good joke! Ó-Ó')
        response = requests.get('https://randomfox.ca/floof/')
        fox = response.json()
        bot.send_photo(message.chat.id, fox['image'])
        
        user.keyboard = telebot.types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True, one_time_keyboard=True)
        user.keyboard.add("Of course! You think I'm crazy??? ❤️", "Nah... I hate foxes and I don't have a heart 💩🔫🦊")
        
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.send_message(message.chat.id, 'Sooo... Another fox? 🥺🥺🥺', reply_markup=user.keyboard) 
        
        bot.register_next_step_handler(msg, choose_step)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, 'I will take this as a request for foxes...')
        response = requests.get('https://randomfox.ca/floof/')
        fox = response.json()
        bot.send_photo(message.chat.id, fox['image'])
        
        user.keyboard = telebot.types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True, one_time_keyboard=True)
        user.keyboard.add("Of course! You think I'm crazy??? ❤️", "Nah... I hate foxes and I don't have a heart 💩🔫🦊")
        
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.send_message(message.chat.id, 'Sooo... Another fox? 🥺🥺🥺', reply_markup=user.keyboard) 
        
        bot.register_next_step_handler(msg, choose_step)
        
        
while True:
    try:    
        bot.polling(none_stop=True)
    except:
        sleep(0.5)
        pass





