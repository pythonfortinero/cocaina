
from operator import eq
global variables
variables = dict()

esigual = eq


flotante = float

entero = int

texto = str

lista = list

dicc = dict

tupla = tuple


def crearVariable(x):
    """Cosas locas."""
    return lambda: variables.update({x: None})


def asignarA(clave, valor):
    return lambda: variables.update({clave: valor()}) if not isinstance(valor, (str, int, float)) else variables.update({clave: valor})


def sumarA(a, b):
    return lambda: variables.update({a: variables[a] + b if isinstance(b, (int, float)) else variables[b]})


def porCada(algo, tupla):
    return lambda: [[elem() for elem in tupla] for a in algo]


def si(condicion, tupla, sino=None):
    return definir(tupla=tupla) if condicion else definir(tupla=sino) if sino else lambda: False 


def devolver(a):
    return lambda: variables[a]


def definir(tupla=None, como=None):
    if not como:
        return lambda: list(map(lambda x: x() if x else x, tupla))[-1]
    else:
        variables[como] = lambda: list(map(lambda x: x(), tupla))[-1]
    return


def usar(nombre):
    return variables[nombre]


def ejecutar(x, parametros={}):
    variables.update(parametros)
    return variables[x]()


def parametro(x):
    return lambda: variables[x]


def crearParametro(clave, valor):
    pass


def HTML():
    pass


def crearRuta():
    pass


def servidor():
    pass

