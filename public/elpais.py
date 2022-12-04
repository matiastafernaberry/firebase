#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psycopg2
import requests, traceback, time, json
import pymysql
import socket
from classifier import *

from datetime import datetime, timezone
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from bs4 import BeautifulSoup
from newspaper import Article, ArticleException
#import nltk
#nltk.download('punkt')
#from pysentimiento import create_analyzer
#analyzer = create_analyzer(task="sentiment", lang="es")
import createfile as create_file


USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}
host = socket.getfqdn()
addr = "192.168.1.122" #socket.gethostbyname(host)
localhost = "192.168.1.122"


class ElpaisScrapperClass():
    """scrapp el pais"""
    # def get(self, request):
    #     resp = requests.get("https://www.elpais.com.uy/", headers=headers)
    #     soup = BeautifulSoup(resp.text, "html.parser")
    #     if resp.status_code == 200:
    #         lista = []
    #         soup = BeautifulSoup(resp.content, "html.parser")
    #         fecha = datetime.now(timezone.utc)
    #         count = 0
    #         for g in soup.find_all('article', class_='articleModule'):
    #             for data in g.find_all('a', href=True):
    #                 try:
    #                     url = "https://www.elpais.com.uy" + data['href']
    #                     if url not in lista:
    #                         lista.append(url)
    #                         article = Article(url, 'es')
    #                         article.download()
    #                         article.parse()
    #                         article_text = article.text
    #                         resp = requests.get(url, headers=headers)
    #                         soup = BeautifulSoup(resp.content, "html.parser")
    #                         try: titulo = soup.select('h1.title')[0].text.strip()
    #                         except:
    #                             titulo = "" 
    #                             print(traceback.format_exc())
    #                         try: subtitulo = soup.select('h2.epigraph')[0].text.strip()
    #                         except:
    #                             subtitulo = ""
    #                             print(traceback.format_exc())
    #                         try: imagen = soup.select('figure.image > img')[0]["data-src"]
    #                         except:
    #                             imagen = ""
    #                             print(traceback.format_exc())

    #                         #print(" ")
    #                         #print(imagen)
    #                         #print(article_text[230:].split('\t'))

    #                         col = {
    #                             "texto":article_text[230:], 
    #                             "url": url,
    #                             "titulo": titulo,
    #                             "subtitulo": subtitulo,
    #                             "imagen": imagen,
    #                             "fecha": fecha,
    #                             "pagina": "elpais",
    #                             "posicion": count
    #                         }
    #                         count += 1
    #                         print(" ")
    #                         print(" ")
    #                         if (count > 5): break
    #                         #print(" --------------------------------------------------------------------- ")
    #                         print(count)
    #                         print(" ")
                            
    #                 except: print(traceback.format_exc())
    #     return TemplateResponse(request, 'index.html', {'lista_paises': 'form'})

    def scrapp(self):
        resp = requests.get("https://www.elpais.com.uy/", headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        if resp.status_code == 200:
            articulosElpais = []
            listaUrls = []
            soup = BeautifulSoup(resp.content, "html.parser")
            fecha = datetime.now(timezone.utc)
            fecha = fecha.strftime("%m/%d/%Y, %H:%M:%S")
            count = 0
            for g in soup.find_all('article', class_='articleModule'):
                #print(" -- g -- ")
                #print(g)
                #print(" -- g -- ")
                #print(" ")
                for data in g.find_all('a', href=True):
                    try:
                        #print(data['href'])
                        url = "https://www.elpais.com.uy" + data['href']
                        article = Article(url, 'es')
                        article.download()
                        article.parse()
                        article_text = article.text
                        #
                        resp = requests.get(url, headers=headers)
                        soup = BeautifulSoup(resp.content, "html.parser")
                        try: titulo = soup.select('h1.title')[0].text.strip()
                        except:
                            titulo = "" 
                            print(traceback.format_exc())
                        try: subtitulo = soup.select('h2.epigraph')[0].text.strip()
                        except:
                            subtitulo = ""
                            print(traceback.format_exc())
                        try: imagen = soup.select('figure.image > img')[0]["data-src"]
                        except:
                            imagen = ""
                            print(traceback.format_exc())
                        #article_text.replace("Contenido Exclusivo La nota a la que intentas acceder es exclusiva para suscriptores Suscribirme ConocÃ© nuestros planes\n\ny disfrutÃ¡ de El PaÃ­s sin lÃ­mites.", " ")
                        #article_text.replace("Ingresar Si ya sos suscriptor podÃ©s\n\ningresar con tu usuario y contraseÃ±a.", " ")
                        #article_text.replace("ingresar con tu usuario y contraseña.", " ")
                        #print(" ")
                        #print(imagen)
                        #print(article_text[230:].split('\t'))
                        
                        if url not in listaUrls:
                            listaUrls.append(url)
                            #
                            nameFile = "-".join(titulo.split())
                            nameFile = ''.join(e for e in nameFile if e.isalnum())
                            def normalize(s):
                                replacements = (
                                    ("á", "a"),
                                    ("é", "e"),
                                    ("í", "i"),
                                    ("ó", "o"),
                                    ("ú", "u"),
                                )
                                for a, b in replacements:
                                    s = s.replace(a, b).replace(a.upper(), b.upper())
                                return s
                            nameFile = normalize((nameFile.lower()))
                            col = {
                                "texto": article_text[230:], 
                                "url": url,
                                "titulo": titulo,
                                "subtitulo": subtitulo,
                                "imagen": imagen,
                                "fecha": fecha,
                                "pagina": "elpais",
                                "posicion": count,
                                "nameFile" : nameFile + ".html"
                            }
                            articulosElpais.append(col)
                            count += 1
                            create_file.createFile(subtitulo, imagen, url, titulo, article_text[230:])
                            #print(" ")
                            #print(" ")
                            #print(col)
                            col = {}
                            #if (count > 5): break
                            print(count)
                            print(" ")
                            print(" ")
                            #break
                    except: print(traceback.format_exc())
                #if (count > 5): break
            # end for
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            final = json.dumps(articulosElpais, indent=2)
            with open("articulosElpais-"+ str(current_time) +".json",'w', encoding = 'utf-8') as f:
                f.write(str(final))


if __name__ == "__main__":  
    elpais = ElpaisScrapperClass()
    elpais.scrapp()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
else:
    elpais = ElpaisScrapperClass()
    elpais.scrapp()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)