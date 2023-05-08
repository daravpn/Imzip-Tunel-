import telebot
import os
import time
from telethon import TelegramClient, events, types
from typing import Tuple
from Crypto.Cipher import AES
from base64 import b64decode
from urllib.parse import unquote

tok="6011914153:AAHUdtuEM6Spdh5yHB2SrKtI8Ms-YNtGj9o" 
bot = telebot.TeleBot(tok)

def armodvpn(key:str|bytes='artunnel57122611', config_encrypt:str='') -> str:
    key = key.encode('utf-8')

    if 'ar-ssh://' in config_encrypt:
        try:
            ciphertext = b64decode(config_encrypt.split('ar-ssh://')[1])
        except:
            return '[>] Invalid config.'
    elif 'ar-vless://' in config_encrypt:
        try:
            ciphertext = b64decode(config_encrypt.split('ar-vless://')[1])
        except:
            return '[>] Invalid config.'
    elif 'ar-vmess://' in config_encrypt:
        try:
            ciphertext = b64decode(config_encrypt.split('ar-vmess://')[1])
        except:
            return '[>] Invalid config.'
    elif 'ar-trojan://' in config_encrypt:
        try:
            ciphertext = b64decode(config_encrypt.split('ar-trojan://')[1])
        except:
            return '[>] Invalid config.'
    else:
        return '[>] Invalid config.'
       
    cipher = AES.new(key, AES.MODE_ECB)
    plain_encoded = cipher.decrypt(ciphertext).decode()
    full_decoded = unquote(plain_encoded)
    
    return '[>] Decrypted config ⦔ ' + full_decoded

def receive_telegram_message(message: telebot.types.Message) -> Tuple[str, str]:
    # mendapatkan username pengirim pesan
    username = message.from_user.username

    # mendapatkan teks pesan yang diterima
    pesan = message.text

    return (username, pesan)
    
@bot.message_handler(commands=['start']) 
def welcome(message) :
    bot.send_message(message.chat.id, "BOT AUTO DECRYPT By KMKZ™ Tools\n=================================\n•TNL\n•ZIV\n•SSH\n") 

@bot.message_handler(commands=['menu']) 
def menu(message) :
    bot.send_message(message.chat.id, "mau apa bangsat") 

@bot.message_handler(commands=['list']) 
def list(message) :
    bot.send_message(message.chat.id, "yah wahyu") 

@bot.message_handler(content_types=['document']) 
def post(message):
    print(message) 
    name=message.document.file_name 
    
    id=message.document.file_id
    file_info = bot.get_file(id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    jj=open(name,"wb") 
    jj.write(downloaded_file)
    jj.close()    
    os.system('python entrykey.py "'+name+'" > test.txt')
    jh=open("test.txt").read()
    bot.reply_to(message, jh)

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    username, pesan = receive_telegram_message(message)

    if 'ar-' in pesan:
        hasil = armodvpn(config_encrypt=pesan)
        bot.reply_to(message, hasil)
    elif message.chat.type == "private":
        bot.reply_to(message, message.text)
    elif message.chat.type == "private":
        if('@Dectnl_bot' in message.text):
            bot.reply_to(message, "Hello to all!")
    else:
        bot.reply_to(message, 'Pesan yang Anda kirimkan tidak valid.')

print('BOT BERJALAN')
print("JAGAN LUPA TURU") 
bot.polling() 

