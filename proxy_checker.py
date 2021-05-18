import urllib.request , socket
import requests
import sys
api = "http://ip-api.com/json/"

socket.setdefaulttimeout(120)   #temps d'attente max (2 min) durant lequel le proxy va essayer de se connecter au site web 

sys.stdout.flush()

def proxy_test(pip):   
    """test du proxy afin de savoir si celui ci est valide. on l'utilise sur mozilla puis on le connecte sur google.com.
     si cela fonctionne on renvoie via index.py, le faite que le proxy fonctionne et le pays ou il est heberger"""
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        #connection du proxy 
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]    #utilisation sur mozilla 
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')    #test de connection sur google.com (vous pouvez changer pour le site que vous voulez )
    
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code                   #code d'erreur si le programme na pas reussi a se connecter au site (donc proxy invalid)
    except Exception as detail:

        print( "ERROR:", detail)
        return 1                 # -> envoie du detaille de l'erreur (si erreur chelou )
    return 0

