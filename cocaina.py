
from __future__ import print_function
from operator import eq
from copy import deepcopy

global variables, ultimosParametros, variablesLocales
variables = dict()
variablesLocales = dict()
ultimosParametros = dict()

esigual = eq

flotante = float

entero = int

cadena = str

lista = list

dicc = dict

tupla = tuple


def analizadorDeCadenas(valor):
    globales = globals()
    valorSeparado = valor.split()
    return " ".join(map(lambda x: str(x) if "%%" not in x else str(globales["variables"][x.replace("%%", "")]), valorSeparado))


def analizadorDeTupla(valor):
    return ", ".join(map(lambda x: analizadorDeCadenas(x), valor))


def generadorDeOutput(valor=""):
    return analizadorDeTupla(valor) if isinstance(valor, (tupla, lista)) else analizadorDeCadenas(valor)


def imprimir(valor):
    return lambda: print(generadorDeOutput(valor))


def crear(x, valor=None):
    return lambda: variables.update({x: valor})


def asignar(clave, valor):
    return lambda: variables.update({clave: valor()}) if not isinstance(valor, (str, int, float)) else variables.update({clave: valor})


def sumar(a, b):
    return lambda: variables.update({a: variables[a] + b if isinstance(b, (int, float)) else variables[b]})


def restar(a, b):
    return lambda: variables.update({a: variables[a] - b if isinstance(b, (int, float)) else variables[b]})


def multiplicar(a, b):
    return lambda: variables.update({a: variables[a] * b if isinstance(b, (int, float)) else variables[b]})


def dividir(a, b):
    return lambda: variables.update({a: variables[a] / b if isinstance(b, (int, float)) else variables[b]})


def resto(a, b):
    return lambda: variables.update({a: variables[a] % b if isinstance(b, (int, float)) else variables[b]})


def porCada(algo, tupla):
    return lambda: [[elem() for elem in tupla] for a in algo]


def si(condicion, tupla, sino=None):
    return definir(tupla=tupla) if condicion else definir(tupla=sino) if sino else lambda: False


def devolver(a):
    return lambda: variables[a]


def usar(nombre, parametros={}):
    ultimosParametros = deepcopy(parametros)
    return lambda: variables[nombre]


def usarLocal(nombre, parametros={}):
    ultimosParametros = deepcopy(parametros)
    return lambda: variablesLocales[nombre]


def crearEnLocal(nombre, valor=None):
    return lambda: variablesLocales.update({nombre: valor})


def ejecutar(x, parametros={}):
    globales = globals()
    preVariablesLocales = globales["variablesLocales"]
    globales["variablesLocales"] = {}
    globales["variablesLocales"].update(globales["parametros"])
    resultado = globales["variables"][x]()
    globales["variableLocales"] = preVariablesLocales
    return resultado


def ejecutarInstruccion(x):
    globales = globals()
    preVariablesLocales = globales["variablesLocales"]
    globales["variablesLocales"] = {}
    if globales["ultimosParametros"]:
        globales["variablesLocales"].update(globales["ultimosParametros"])
        del globales["ultimosParametros"]
    resultado = x()
    globales["variableLocales"] = preVariablesLocales
    return resultado


def definir(tupla=None, como=None):
    if not como:
        return lambda: list(map(lambda x: ejecutarInstruccion(x), tupla))[-1]
    else:
        variables[como] = lambda: list(map(lambda x: ejecutarInstruccion(x), tupla))[-1]
    return


def parametro(x):
    return lambda: variablesLocales[x]


def crearParametro(clave, valor):
    pass


def HTML():
    pass


def crearRuta():
    pass


def servidor():
    pass
