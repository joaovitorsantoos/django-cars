from django.shortcuts import render
from django.http import HttpResponse


def cars_view(request):
    html = '''
    <html>
        <head>
            <title>TJ - Carros</title>
        </head>
        <body>
            <h1>Carros mais vendidos</h1>
            <h3>Compre ja o seu!</h3>
        </body>
    </html>

'''
    return HttpResponse(html)
    
