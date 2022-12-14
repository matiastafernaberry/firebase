#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timezone


def createFile(description, image, url, title, content):
    content = content.replace(".", ".<br><br>")
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
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
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
                <p>
                    fuente: <a href="{url}">{url}</a>
                </p>
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
            ("??", "a"),
            ("??", "e"),
            ("??", "i"),
            ("??", "o"),
            ("??", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    nameFile = normalize((nameFile.lower()))
    with open(nameFile + ".html",'w', encoding = 'utf-8') as f:
        f.write(contentFile)




if __name__ == "__main__":
    # description = 'La legisladora nacionalista consider?? que est?? en riesgo la Rep??blica y calific?? al presidente V??zquez como "autoritario disimulado"'
    # image = "https://noticias-uruguay.firebaseapp.com/elobservador/bianchiiii.jpg"
    # url = "https://noticias-uruguay.firebaseapp.com/elobservador/"
    # title = "Diputada Bianchi pidi?? elecciones anticipadas"
    # content = """
    # <p>
    #     La diputada Graciela Bianchi (Partido Nacional) 
    #     cuestion?? al presidente Tabar?? V??zquez por haber decidido la 
    #     esencialidad de la educaci??n 
    #     y lo calific?? de "autoritario disimulado" que en su opini??n "son los peores".
    # </p>
    # <p>
    #     La legisladora, que estuvo al frente del Liceo Bauz?? y es recordada por haberle pedido respeto a los estudiantes que entraron a su oficina, 
    #     advirti?? que la situaci??n actual del pa??s es para que haya "elecciones anticipadas".
    # </p>
    # <p>
    #     Entrevistada este viernes por Mariano L??pez en 
    #     El Observador TV, Bianchi consider?? que "est?? en riesgo la Rep??blica".
    # </p>
    # <p>
    #     "Yo que soy partidaria de una democracia parlamentaria, no presidencialista, estamos en una situaci??n para elecciones anticipadas"
    # </p>
    # <p>
    #     <span id="saysCMSEmphasisaeslbquvwiwfjemi" class="">
    #         "Diga que en Uruguay estamos en un Rep??blica presidencialista y la seguiremos remando", 
    #         afirm?? Bianchi.</span>
    # </p>
    # <p>
    #     El periodista le pregunto si "la cosa es tan grave" como para que adelantar los comicios. 
    #     "Es grav??sima la situaci??n. Lo que pasa es que se barri?? debajo de la alfombra", respondi??.
    # </p>
    # <p>
    #     La diputada aclar?? que sus expresiones no comprometen al Partido Nacional y menos a Luis Lacalle Pou, l??der del sector Todos 
    #     al que ella pertenece.
    # </p>
    # """

    #createFile(description, image, url, title, content)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
else:
    # description = 'La legisladora nacionalista consider?? que est?? en riesgo la Rep??blica y calific?? al presidente V??zquez como "autoritario disimulado"'
    # image = "https://noticias-uruguay.firebaseapp.com/elobservador/bianchiiii.jpg"
    # url = "https://noticias-uruguay.firebaseapp.com/elobservador/"
    # title = "Diputada Bianchi pidi?? elecciones anticipadas"
    # content = """
    # <p>
    #     La diputada Graciela Bianchi (Partido Nacional) 
    #     cuestion?? al presidente Tabar?? V??zquez por haber decidido la 
    #     esencialidad de la educaci??n 
    #     y lo calific?? de "autoritario disimulado" que en su opini??n "son los peores".
    # </p>
    # <p>
    #     La legisladora, que estuvo al frente del Liceo Bauz?? y es recordada por haberle pedido respeto a los estudiantes que entraron a su oficina, 
    #     advirti?? que la situaci??n actual del pa??s es para que haya "elecciones anticipadas".
    # </p>
    # <p>
    #     Entrevistada este viernes por Mariano L??pez en 
    #     El Observador TV, Bianchi consider?? que "est?? en riesgo la Rep??blica".
    # </p>
    # <p>
    #     "Yo que soy partidaria de una democracia parlamentaria, no presidencialista, estamos en una situaci??n para elecciones anticipadas"
    # </p>
    # <p>
    #     <span id="saysCMSEmphasisaeslbquvwiwfjemi" class="">
    #         "Diga que en Uruguay estamos en un Rep??blica presidencialista y la seguiremos remando", 
    #         afirm?? Bianchi.</span>
    # </p>
    # <p>
    #     El periodista le pregunto si "la cosa es tan grave" como para que adelantar los comicios. 
    #     "Es grav??sima la situaci??n. Lo que pasa es que se barri?? debajo de la alfombra", respondi??.
    # </p>
    # <p>
    #     La diputada aclar?? que sus expresiones no comprometen al Partido Nacional y menos a Luis Lacalle Pou, l??der del sector Todos 
    #     al que ella pertenece.
    # </p>
    # """

    #createFile(description, image, url, title, content)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)