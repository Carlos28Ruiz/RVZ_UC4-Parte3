from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
layout = """
    <h1> UA4 (LP3) | Ruiz_Vasquez_Zevallos </h1>
    <hr/>
    <ul>
        <li>
            <a href="/integrantes"> integrantes</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
    </ul>
    <hr/>
"""


def integrantes(request):
    mensaje ="""
        <h1>Integrantes</h1>
        <ul>
            <li>Ruiz Montero Carlos</li>
            <li>Vasquez Leyva Antony</li>
            <li>Zevallos Torres Diego</li>
        </ul>
    """
    return render(request, 'integrantes.html')
def saludo(request):
    mensaje ="Hola Este es el UA4 "
    return render(request, 'saludo.html')