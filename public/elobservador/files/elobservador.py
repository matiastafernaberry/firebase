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


class ElobservadorScrapperClass():
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
        resp = requests.get("https://www.elobservador.com.uy/", headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        if resp.status_code == 200:
            articulosElpais = []
            listaUrls = []
            soup = BeautifulSoup(resp.content, "html.parser")
            fecha = datetime.now(timezone.utc)
            fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
            count = 0
            for g in soup.find_all('div', class_='nota'):
                #print(" -- g -- ")
                #print(g)
                #print(" ")
                #print(" ")
                print(" ")
                print(" ")
                print(" ")
                for data in g.find_all('a', href=True):
                    print(data['href'])
                    url = "https://www.elobservador.com.uy" + data['href']
                    try:
                        article = Article(url, 'es')
                        article.download()
                        article.parse()
                        article_text = article.text
                    except:
                        article_text = ""
                        print(traceback.format_exc())

                    try:
                        resp = requests.get(url, headers=headers)
                        soup = BeautifulSoup(resp.content, "html.parser")
                    except: continue
                    #
                    try: titulo = soup.find(class_='titulo').text
                    except:
                        titulo = ""
                        print(traceback.format_exc())
                    #
                    try: subtitulo = soup.find('p' ,class_='intro').text
                    except:
                        subtitulo = ""
                        print(traceback.format_exc())
                    #
                    try: 
                        imagen = soup.find('div', class_ = "imggal")
                        imagen = imagen.find('img')
                        imagen = imagen["data-src"].split("?")[0]
                        imagen = str(imagen) + "?&amp;cw=350&amp;ch=213"
                    except:
                        imagen = ""
                        print(traceback.format_exc())
                    #print(" ")
                    #print(str(imagen) + "?&amp;cw=350&amp;ch=213")
                    #print(" ")
                    #print(" ")
                    #print(" ")
                    #print(" ")
                    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
                    fecha = datetime.now(timezone.utc)
                    fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
                    fecha = fecha.split(",")[0]
                    mes = fecha.split("-")[1]
                    mesActual = meses[int(mes)-1]
                    fecha = fecha.split("-")[0] + " " + mesActual + " de " + fecha.split("-")[2]


                    if url not in listaUrls:
                        listaUrls.append(url)
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
                        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
                        fecha = datetime.now(timezone.utc)
                        fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
                        fecha = fecha.split(",")[0]
                        mes = fecha.split("-")[1]
                        mesActual = meses[int(mes)-1]
                        fecha = fecha.split("-")[0] + mesActual + fecha.split("-")[2]
                        col = {
                            "texto": article_text, 
                            "url": url,
                            "titulo": titulo,
                            "subtitulo": subtitulo,
                            "imagen": imagen,
                            "fecha": fecha,
                            "pagina": "elobservador",
                            "posicion": count,
                            "nameFile" : "files/" + fecha + "-"  + nameFile + ".html"
                        }
                        articulosElpais.append(col)
                        count += 1
                        print(count)
                        create_file.createFile(subtitulo, imagen, url, titulo, article_text, fecha)


                    break
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            final = json.dumps(articulosElpais, indent=2, ensure_ascii=False)
            print("  escribiendo el archivo  ")
            print("   ")
            with open("articulosElobservador-"+ str(current_time) +".json",'w', encoding = 'utf-8') as f:
                f.write(str(final))


if __name__ == "__main__":  
    elobservador = ElobservadorScrapperClass()
    elobservador.scrapp()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
else:
    elobservador = ElobservadorScrapperClass()
    elobservador.scrapp()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)