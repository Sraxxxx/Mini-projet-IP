from colorama import init, Fore
from colorama.initialise import reset_all
import requests
import sys

init()



api = "http://ip-api.com/json/"   #api qui permet de recuperer toutes les infos de iplocation() grace a l'ip 
 

def iplocation(ip): 
        """recuperation des donner de l'ip (operateur, organisation (c'est pour les entreprise), ville, region, pays.)
        on donne aussi la longitude et latitude de la ville en question et son fuseau horaire"""


        
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        
        print("")
        print (Fore.LIGHTGREEN_EX + "[Ip]:", data['query'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Operateur]:", data['isp'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Organisation]:", data['org'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Ville]:", data['city'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Region]:", data['region'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Code postal]:", data['zip'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Pays]:", data['country'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Longitude]:", data['lon'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Latitude]:", data['lat'])
        print("")
        print (Fore.LIGHTGREEN_EX +  "[Time zone]:", data['timezone'])
        print("")
        
        