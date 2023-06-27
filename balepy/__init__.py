import requests
from colorama import Fore
from sys import exit


print(f"""Wellcom to{Fore.MAGENTA} balepy {Fore.RESET} library version:{Fore.LIGHTBLUE_EX} 0.6 {Fore.RESET}
{Fore.GREEN}Mohammad Mehrabi Rad{Fore.RESET} and {Fore.RED}Erfan Bafandeh{Fore.RESET}{Fore.LIGHTMAGENTA_EX} <github.com/OnlyRad>{Fore.RESET}\n""")

class Bot:
    #
    def __init__(self , token:str):
        a = requests.get(f"https://tapi.bale.ai/bot{token}/deleteWebhook")
        a = a.json()
        a = a['ok']
        b = "Token not found"
        if a == False:
        	print(b)
        	exit()
        else:
        	self.token = token
    #
    def send_Message(self , chat_id:int , text:str):
        text.replace(" ", "+")
        a = requests.get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}")
        return a
	#
    def getupdate(self):
        a = requests.get(f"https://tapi.bale.ai/bot{self.token}/getupdates")
        a = a.json()
        a = a['result']
        return a
	#
    def get_lastupdate(self):
        a = requests.get(f"https://tapi.bale.ai/bot{self.token}/getupdates")
        a = a.json()
        a = a['result']
        ac = len(a)
        ac = ac - 1
        a = a[ac]
        return a
	#
    def getme(self):
        a = requests.get(f"https://tapi.bale.ai/bot{self.token}/getme")
        return a
    #
    def getchat(self , chat_id):
        a = requests.get(f"https://tapi.bale.ai/bot{self.token}/getchat?chat_id={chat_id}")
        return a
    #
    def edit_Message(self, chat_id:int, message_id:int, text:str):
    	text.replace(" ", "+")
    	a = requests.get(f"https://tapi.bale.ai/bot{self.token}/editmessagetext?chat_id={chat_id}&message_id={message_id}&text={text}")
    	return a
    #
    def delete_Message(self, chat_id:int, message_id:int):
    	a = requests.get(f"https://tapi.bale.ai/bot{self.token}/deletemessage?chat_id={chat_id}&message_id={message_id}")
    	return a
    #
    def get_chat_admin(self, chat_id:int):
    	a = requests.get(f"https://tapi.bale.ai/bot{self.token}/getChatAdministrators?chat_id={chat_id}")
    	return a
    
