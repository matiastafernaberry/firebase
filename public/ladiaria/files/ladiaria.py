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


class LadiariaScrapperClass():
    """scrapp la diaria"""
    def scrapp(self):
        resp = requests.get("https://ladiaria.com.uy/", headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        if resp.status_code == 200:
            articulosElpais = []
            listaUrls = []
            soup = BeautifulSoup(resp.content, "html.parser")
            fecha = datetime.now(timezone.utc)
            fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
            count = 0
            for g in soup.find_all('div', class_='ld-card'):
                print(" -- g -- ")
                print(" ")
                link  = g.find('a', href=True)['href']
                url = "https://ladiaria.com.uy" + link
                print(url)
                print(count)
                print(" ")
                count += 1
                #
                article = Article(url, 'es')
                article.download()
                article.parse()
                article_text = article.text
                print(article_text)
                print(" ")
                print(" ")
                print(" ")
                #resp = requests.get(url, headers=headers)
                #soup = BeautifulSoup(resp.content, "html.parser")
                #print(" ")
                #print(soup)
                #try: titulo = soup.select('h1.title')[0].text.strip()
                #except:
                #    titulo = "" 
                #    print(traceback.format_exc())

                if count == 15: break
                #print(" -- g -- ")
                #print(" ")
                #for data in g.find_all('a', href=True):
            #         try:
            #             #print(data['href'])
            #             url = "https://ladiaria.com.uy/" + data['href']
            #             article = Article(url, 'es')
            #             article.download()
            #             article.parse()
            #             article_text = article.text
            #             #
            #             resp = requests.get(url, headers=headers)
            #             soup = BeautifulSoup(resp.content, "html.parser")
            #             try: titulo = soup.select('h1.title')[0].text.strip()
            #             except:
            #                 titulo = "" 
            #                 print(traceback.format_exc())
            #             try: subtitulo = soup.select('h2.epigraph')[0].text.strip()
            #             except:
            #                 subtitulo = ""
            #                 print(traceback.format_exc())
            #             try: imagen = soup.select('figure.image > img')[0]["data-src"]
            #             except:
            #                 imagen = ""
            #                 print(traceback.format_exc())
            #             #article_text.replace("Contenido Exclusivo La nota a la que intentas acceder es exclusiva para suscriptores Suscribirme ConocÃ© nuestros planes\n\ny disfrutÃ¡ de El PaÃ­s sin lÃ­mites.", " ")
            #             #article_text.replace("Ingresar Si ya sos suscriptor podÃ©s\n\ningresar con tu usuario y contraseÃ±a.", " ")
            #             #article_text.replace("ingresar con tu usuario y contraseña.", " ")
            #             #print(" ")
            #             #print(imagen)
            #             #print(article_text[230:].split('\t'))
            #             meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            #             fecha = datetime.now(timezone.utc)
            #             fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
            #             fecha = fecha.split(",")[0]
            #             mes = fecha.split("-")[1]
            #             mesActual = meses[int(mes)-1]
            #             fecha = fecha.split("-")[0] + " " + mesActual + " de " + fecha.split("-")[2]
            #             #print(fecha)
            #             #print(" ")
                        
            #             if url not in listaUrls:
            #                 listaUrls.append(url)
            #                 #
            #                 nameFile = "-".join(titulo.split())
            #                 nameFile = ''.join(e for e in nameFile if e.isalnum())
            #                 def normalize(s):
            #                     replacements = (
            #                         ("á", "a"),
            #                         ("é", "e"),
            #                         ("í", "i"),
            #                         ("ó", "o"),
            #                         ("ú", "u"),
            #                     )
            #                     for a, b in replacements:
            #                         s = s.replace(a, b).replace(a.upper(), b.upper())
            #                     return s
            #                 nameFile = normalize((nameFile.lower()))
            #                 meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            #                 fecha = datetime.now(timezone.utc)
            #                 fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
            #                 fecha = fecha.split(",")[0]
            #                 mes = fecha.split("-")[1]
            #                 anio = fecha.split("-")[2]
            #                 dia = fecha.split("-")[0]
            #                 mesActual = meses[int(mes)-1]
            #                 fecha = dia + mesActual + anio
                            
            #                 col = {
            #                     "texto": article_text[230:], 
            #                     "url": url,
            #                     "titulo": titulo,
            #                     "subtitulo": subtitulo,
            #                     "imagen": imagen,
            #                     "fecha": fecha,
            #                     "pagina": "elpais",
            #                     "posicion": count,
            #                     "nameFile" : "files/" + anio + "/" + mes + "/" + dia + "/" + nameFile + ".html"
            #                 }
            #                 articulosElpais.append(col)
            #                 count += 1
            #                 fecha = dia + " " + mesActual + " de " + anio
            #                 create_file.createFile(subtitulo, imagen, url, titulo, article_text[230:], fecha)
            #                 #print(" ")
            #                 #print(" ")
            #                 #print(col)
            #                 col = {}
            #                 #if (count > 5): break
            #                 print(count)
            #                 print(" ")
            #                 print(" ")
            #                 #break
            #         except: print(traceback.format_exc())
            #     #if (count > 5): break
            # # end for
            # now = datetime.now()
            # current_time = now.strftime("%H:%M:%S")
            # final = json.dumps(articulosElpais, indent=2)
            # nameFileLog = "articulosElpais-"+ str(current_time) +".json"
            # with open(nameFileLog, 'w', encoding = 'utf-8') as f:
            #     f.write(str(final))
            # return nameFileLog
        
    # def createIndex(self, nameFileLOg):
    #     final = ""
    #     meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    #     fecha = datetime.now(timezone.utc)
    #     fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
    #     fecha = fecha.split(",")[0]
    #     mes = fecha.split("-")[1]
    #     mesActual = meses[int(mes)-1]
    #     fecha = fecha.split("-")[0] + " " + mesActual + " de " + fecha.split("-")[2]
    #     with open(nameFileLOg, encoding='utf-8') as fh:
    #         dataJson = json.load(fh)
    #     contentFile = """
    #         <!DOCTYPE html>
    #         <html>
    #         <head>
    #             <meta charset="utf-8">
    #             <meta charset="utf-8">
    #             <meta name="viewport" content="width=devicele-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    #             <meta http-equiv="content-language" contconent="es" />
                
    #             <link rel="stylesheet" href="bootstrap.css">
    #             <link rel="stylesheet" href="bootstrap-grid.css">
    #             <script src="jquery-3.6.1.min.js"></script>
    #             <script src="bootstrap.js"></script>
    #             <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Noto+Sans">
    #             <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nerko+One">
    #             <title>MilangaConSalmon</title>
    #         </head>
    #         <body>
    #             <nav class="navbar navbar-expand-lg navbar-light ">
    #             <a class="navbar-brand" href="/" style="font-family: 'Nerko One';font-size: 30px;color: #0289CB;">Noticias de Uruguay y el mundo</a>
    #             <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    #                 <span class="navbar-toggler-icon"></span>
    #             </button>
    #             <div class="collapse navbar-collapse float-right justify-content-end" id="navbarNav">
    #                 <ul class="navbar-nav">
    #                 <li class="nav-item active">
    #                     <a class="nav-link" href="../elpais/index.html" style="font-family: 'Nerko One';font-size: 20px;color: #0289CB;">El País <span class="sr-only">(current)</span></a>
    #                 </li>
    #                 <li class="nav-item active">
    #                     <a class="nav-link" href="../elobservador/index.html" style="font-family: 'Nerko One';font-size: 20px;color: #0289CB;">El Observador<span class="sr-only">(current)</span></a>
    #                 </li>
    #                 </ul>
    #             </div>
    #             </nav>
    #             <div class="container">
    #             <div class="row">
    #                 <div class="col-sm">
    #                 <p class="intro" itemprop="description">
    #                     <h3 style="color: #0289CB;font-family: 'Nerko One';">Noticias de elpais.com.uy {fecha}</h3>
    #                 </p>
    #                 </div>
    #             </div>
    #             </div>
    #             <div id="contenido">

    #             </div>
    #             <div class="container">
    #             <div class="row">
    #                 <div class="col-sm">
                    
    #                 </div>
    #             </div>
    #             </div>
    #             <script>
    #             const texto = {dataJson}
    #             const result = JSON.stringify(texto)
    #             const obj = JSON.parse(result);
    #             console.log(obj);
    #         """.format(
    #             dataJson = dataJson,
    #             fecha = fecha
    #         )
    #     with open("../index.html", 'w', encoding = 'utf-8') as f:
    #             f.write(contentFile)
    #     restOfText = """
    #         var html="<div class='container'>";
    #             html+= "<div class='row'>";
    #             var count = 0;
    #             for (let value of obj) {
    #                 if (count > 1){
    #                     html+= "<div class='col-xs-6 col-sm-4 col-md-4'";
    #                     html+= "<p><img src="+value.imagen+" class='img-fluid'></p>";
    #                     html+= "<p><a href='"+value.nameFile+"'><h4 id='titulo' style='font-weight: bold;'>"+value.titulo+"</h4></a></p>";
    #                     html+= "<p><h5 id='subtitulo' style='font-family: Montserrat;'>"+value.subtitulo+"</h5></p>";
    #                     html+= "<br>";
    #                     html+= "</div>";
    #                 }
    #                 count = count + 1;
    #             }
    #             html+= "</div>";
    #             html+= "</div>";
    #             $( "#contenido" ).append( html );
    #             </script>
    #         </body>
    #         </html>
    #     """
    #     with open("../index.html", 'a', encoding = 'utf-8') as f:
    #             f.write(restOfText)
            


if __name__ == "__main__":  
    ladiaria = LadiariaScrapperClass()
    nameFileLOg = ladiaria.scrapp()
    #ladiaria.createIndex(nameFileLOg)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
else:
    ladiaria = LadiariaScrapperClass()
    nameFileLOg = ladiaria.scrapp()
    #ladiaria.createIndex(nameFileLOg)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)