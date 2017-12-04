# prototipos para json
from cocaina import *

definir(a=(
    pedirPorGET("https://api.mercadolibre.com/items/" + parametro("item"),
        guardarEn="variable1"),
    guardarRespuesta("variable1", en="respuesta"),
    si(valor("respuesta", "OK"), (
        devolver(imprimir(json("respuesta")))),
    sino=(
        devolver(imprimir("Fallo la api")),)),),
    como="pedir items por GET a mercadolibre")


definir(a=(
    pedirPorPOST("https://api.mercadolibre.com/items/" + parametro("item"),
        datos={'key1': 'value1', 'key2': 'value2'},
        guardarEn="variable1"),
    guardarRespuesta("variable1", en="respuesta"),
    si(valor("respuesta", "OK"), (
        devolver(imprimir(json("respuesta")))),
    sino=(
        devolver(imprimir("Fallo la api")),)),),
    como="pedir items por POST a mercadolibre")


ejecutar("pedir items por GET a mercadolibre")
ejecutar("pedir items por POST a mercadolibre")