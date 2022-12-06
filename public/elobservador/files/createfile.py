#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timezone


def createFile(description, image, url, title, content, fecha):
    content = list(filter(lambda x : x != '', content.split('\n\n')))
    content = '<br><br>'.join(content)
    #content = content.replace(".", ".<br><br>", 5)
    contentFile = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"/>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>  
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
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
        
        <title>{title}</title>
        <link rel="stylesheet" href="bootstrap.css">
        <link rel="stylesheet" href="bootstrap-grid.css">
        <script src="jquery-3.6.1.min.js"></script>
        <script src="bootstrap.js"></script>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nerko+One">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="/" style="font-family: 'Nerko One';font-size: 30px;color: #0289CB;">Noticias de Uruguay y el mundo</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse float-right justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="../../elpais/index.html" style="font-family: 'Nerko One';font-size: 20px;color: #0289CB;">El País <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="../../elobservador/index.html" style="font-family: 'Nerko One';font-size: 20px;color: #0289CB;">El Observador<span class="sr-only">(current)</span></a>
                </li>
                
                </ul>
            </div>
        </nav>
        <div class="container">
        <div class="row">
            <div class="col-sm">
                <p>
                    <h2>{title}</h2>
                </p>
                <br>
                <p>
                    <h3>{description}</h3>
                </p>
                <br>
                <p>
                    <img src="{image}" alt="" class="img-fluid">
                </p>
                <p>{fecha}</p>
                <br>
                <br>
                    <p>{content}</p>
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
        content = content,
        fecha = fecha
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
    import codecs
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    fecha = datetime.now(timezone.utc)
    fecha = fecha.strftime("%d-%m-%Y, %H:%M:%S")
    fecha = fecha.split(",")[0]
    mes = fecha.split("-")[1]
    mesActual = meses[int(mes)-1]
    fecha = fecha.split("-")[0] + mesActual + fecha.split("-")[2]
    with codecs.open(fecha + "-" + nameFile + ".html", "w", "utf-8") as temp:
        temp.write(contentFile)



if __name__ == "__main__":
    #createFile(description, image, url, title, content)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
else:
    #createFile(description, image, url, title, content)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)