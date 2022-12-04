#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timezone


def createFile(description, image, url, title, content):
    contentFile = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta property="description" content="{description}"/>
        <meta property="og:site_name" content="@milangaconsalm1"/>
        <meta property="og:description" content="{description}"/>
        <meta property="og:image" content="{image}"/>
        <meta property="og:type" content="article"/>
        <meta property="og:url" content="{url}"/>
        <meta property="og:title" content="{title}"/>
        <meta itemprop="url" content="{url}"/>
        <meta itemprop="name" content="{title}"/>
        <meta itemprop="headline" content="{title}"/>
        <meta itemprop="description" content="{description}"/>
        <meta name="twitter:card" content="summary_large_image"/>
        <meta name="twitter:site" content="@milangaconsalm1"/>
        <meta name="twitter:title" content="{title}"/>
        <meta name="twitter:description" content="{description}"/>
        <meta name="twitter:creator" content="@milangaconsalm1"/>
        <meta name="twitter:image" content="{image}"/>
        <meta name="twitter:image:width" content="0"/>
        <meta name="twitter:image:height" content="0"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>  
        <meta charset="UTF-8"/>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>  
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>{title}</title>
        <link rel="stylesheet" href="bootstrap.css">
    </head>
    <body>
        <div class="container">
        <div class="row">
            <div class="col-sm">
                <p>
                    <h1>{title}</h1>
                </p>
                <p>
                    <h2>{description}</h2>
                </p>
                <p>
                    <img src="{image}" alt="" class="img-fluid">
                </p>
                <br>
                <br>
                {content}
                <br>
                <br>
            </div>
        </div>
        </div>
    </body>
    </html>
    """.format(
        description = description, 
        image = image,
        url = url,
        title = title,
        content = content
    )
    nameFile = "-".join(title.split())
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
    with open(nameFile + ".html",'w', encoding = 'utf-8') as f:
        f.write(contentFile)




if __name__ == "__main__":
    # description = 'La legisladora nacionalista consideró que está en riesgo la República y calificó al presidente Vázquez como "autoritario disimulado"'
    # image = "https://noticias-uruguay.firebaseapp.com/elobservador/bianchiiii.jpg"
    # url = "https://noticias-uruguay.firebaseapp.com/elobservador/"
    # title = "Diputada Bianchi pidió elecciones anticipadas"
    # content = """
    # <p>
    #     La diputada Graciela Bianchi (Partido Nacional) 
    #     cuestionó al presidente Tabaré Vázquez por haber decidido la 
    #     esencialidad de la educación 
    #     y lo calificó de "autoritario disimulado" que en su opinión "son los peores".
    # </p>
    # <p>
    #     La legisladora, que estuvo al frente del Liceo Bauzá y es recordada por haberle pedido respeto a los estudiantes que entraron a su oficina, 
    #     advirtió que la situación actual del país es para que haya "elecciones anticipadas".
    # </p>
    # <p>
    #     Entrevistada este viernes por Mariano López en 
    #     El Observador TV, Bianchi consideró que "está en riesgo la República".
    # </p>
    # <p>
    #     "Yo que soy partidaria de una democracia parlamentaria, no presidencialista, estamos en una situación para elecciones anticipadas"
    # </p>
    # <p>
    #     <span id="saysCMSEmphasisaeslbquvwiwfjemi" class="">
    #         "Diga que en Uruguay estamos en un República presidencialista y la seguiremos remando", 
    #         afirmó Bianchi.</span>
    # </p>
    # <p>
    #     El periodista le pregunto si "la cosa es tan grave" como para que adelantar los comicios. 
    #     "Es gravísima la situación. Lo que pasa es que se barrió debajo de la alfombra", respondió.
    # </p>
    # <p>
    #     La diputada aclaró que sus expresiones no comprometen al Partido Nacional y menos a Luis Lacalle Pou, líder del sector Todos 
    #     al que ella pertenece.
    # </p>
    # """

    #createFile(description, image, url, title, content)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
else:
    # description = 'La legisladora nacionalista consideró que está en riesgo la República y calificó al presidente Vázquez como "autoritario disimulado"'
    # image = "https://noticias-uruguay.firebaseapp.com/elobservador/bianchiiii.jpg"
    # url = "https://noticias-uruguay.firebaseapp.com/elobservador/"
    # title = "Diputada Bianchi pidió elecciones anticipadas"
    # content = """
    # <p>
    #     La diputada Graciela Bianchi (Partido Nacional) 
    #     cuestionó al presidente Tabaré Vázquez por haber decidido la 
    #     esencialidad de la educación 
    #     y lo calificó de "autoritario disimulado" que en su opinión "son los peores".
    # </p>
    # <p>
    #     La legisladora, que estuvo al frente del Liceo Bauzá y es recordada por haberle pedido respeto a los estudiantes que entraron a su oficina, 
    #     advirtió que la situación actual del país es para que haya "elecciones anticipadas".
    # </p>
    # <p>
    #     Entrevistada este viernes por Mariano López en 
    #     El Observador TV, Bianchi consideró que "está en riesgo la República".
    # </p>
    # <p>
    #     "Yo que soy partidaria de una democracia parlamentaria, no presidencialista, estamos en una situación para elecciones anticipadas"
    # </p>
    # <p>
    #     <span id="saysCMSEmphasisaeslbquvwiwfjemi" class="">
    #         "Diga que en Uruguay estamos en un República presidencialista y la seguiremos remando", 
    #         afirmó Bianchi.</span>
    # </p>
    # <p>
    #     El periodista le pregunto si "la cosa es tan grave" como para que adelantar los comicios. 
    #     "Es gravísima la situación. Lo que pasa es que se barrió debajo de la alfombra", respondió.
    # </p>
    # <p>
    #     La diputada aclaró que sus expresiones no comprometen al Partido Nacional y menos a Luis Lacalle Pou, líder del sector Todos 
    #     al que ella pertenece.
    # </p>
    # """

    #createFile(description, image, url, title, content)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)