from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from miapp.models import Estudiante

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

def crear_estudiante(request):
    estudiante = Estudiante(
        codigo = "2012352133",
        dni = "14323123",
        nombre = "Juan",
        apepat = "Lévano",
        apemat = "Perez",
        direccion = "Magdalena",
        telefono = "8225678",
        estado = "A",
    )
    estudiante.save()
    return HttpResponse(f"""<h1>Estudiante Registrado:</h1>
                            <strong>Código: </strong>{estudiante.codigo} <br>
                            <strong>DNI: </strong>{estudiante.dni}    <br>
                            <strong>Nombre: </strong>{estudiante.nombre} <br>
                            <strong>Apellido Paterno: </strong>{estudiante.apepat} <br>
                            <strong>Apellido Materno: </strong>{estudiante.apemat} <br>
                            <strong>Dirección: </strong>{estudiante.direccion} <br>
                            <strong>Telf: </strong>{estudiante.telefono} <br>
                            <strong>Estado: </strong>{estudiante.estado}""")
