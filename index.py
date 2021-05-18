##################################################################################
#MIT License                                                                     #
#                                                                                #
#Copyright (c) 2021 H0xtry                                                       #
#                                                                                #
#Permission is hereby granted, free of charge, to any person obtaining a copy    #
#of this software and associated documentation files (the "Software"), to deal   #
#in the Software without restriction, including without limitation the rights    #
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       #
#copies of the Software, and to permit persons to whom the Software is           #
#furnished to do so, subject to the following conditions:                        #
#                                                                                #
#The above copyright notice and this permission notice shall be included in all  #
#copies or substantial portions of the Software.                                 #
#                                                                                #
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      #
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        #
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     #
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          #
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   #
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   #
#SOFTWARE.                                                                       #
##################################################################################


from colorama import init, Fore
from location import iplocation
from proxy_checker import proxy_test
from time import gmtime, strftime
import socket
import requests
import sys
from requests import get


init(autoreset = True)

date = strftime('%Y/%m/%d %H:%M:%S', gmtime())   #donne la date et l'heure ou le programme se lance 
api = "http://ip-api.com/json/"

host = socket.gethostname()     #donne le nom de l'ordinateur (desktop...)
ip_host = get('https://api.ipify.org').text  #ip de l'ordinateur (ipv4 soit ip public)
data = requests.get(api+ip_host).json()
sys.stdout.flush()
pays = data['country']   #donne le pays de l'ip 



banner =Fore.LIGHTMAGENTA_EX + """                                                
               ,--.                        ,--. 
 ,---. ,--.,--.|  ,---.      ,---. ,--.,--.`--'             """ + date + """
| .-. :|  ||  ||  .-.  |    | .-. ||  ||  |,--.             """ + host + """
\   --.'  ''  '|  | |  |    ' '-' ''  ''  '|  |             """ + ip_host + """
 `----' `----' `--' `--'     `---'  `----' `--'             [""" + pays + """]
                                                v0.1
                                                
                                                """
                                                
                                


Menu = Fore.MAGENTA + """★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
|                                                  |
|   [1] Geolocaliser une IP   [2] Tester un proxy  |
|                                                  |
|    [3] Message d'aide        [4] Quitter         |
|                                                  |
★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★

                
                """


aide = Fore.YELLOW + """

A quoi sert ce programe ?

    ce programme sert a tester un proxy et trouver la localisation d'une ip 
    imaginon vous avez achetez des proxy sur un site afin d'etre anonyme sur un site 
    ce programme va vous servire a savoir si votre proxy est fonctionnel ou non 
    imaginon vous avez une ip d'un particulier ou bien une ip d'un site 
    avec ce programme vous avez juste a la rentrer et vous connaitrer 
    la ville, le departement et le pays ou se trouve cette ip et l'operateur qui la possede.
            """



print(banner)

i = 1

while i == 1:
    i = 0
    print(Menu)
    choix = int(input("que voulez vous faire ? "))
    if choix > 4 or choix < 1:
        print("pas de choix avec ce nombre", choix) 
        i = 1

    elif choix == 1:

        ip = input("ip a tester : ")
        iplocation(ip)
        p = input("")
        i = 1

    
    elif choix == 2:
        ip = input("ip : ")
        port = input("port : ")
        print("  ")
        proxyList = [ip + ":" + port]
        data = requests.get(api+ip).json()
        for obj in proxyList:
            if proxy_test(obj):
                print("")
                print (Fore.LIGHTRED_EX +"Proxy Mort", obj)
            else:
                
                print (obj, Fore.LIGHTGREEN_EX + "Fonctionne")
                print("")
                print (Fore.LIGHTGREEN_EX + "[Pays]:", data['country'])
        p = input("")
        i = 1


    elif choix == 3:
        print(aide)
        p = input("")
        i = 1
    
    elif choix == 4:
        pass
    

    







