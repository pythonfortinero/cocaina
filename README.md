# cocaina
Lenguaje de programación adictivo y estimulante

## Ejemplo hola mundo
```python
from cocaina import *

definir((
	imprimir("Hola Mundo!!"),
	), como="principal")

ejecutar("principal")
```

## Ejemplo mas complejo
```python
from cocaina import *

definir((
    sumarA("x", -5),
), como="restar")

definir((
    crearVariable("x"),
    asignarA("x", parametro("a")),
    sumarA("x", 5),
    usar("restar"),
    si(esigual(6, 5),
        (crearVariable("z"),
        asignarA("z", 5)),
    sino=(crearVariable("d"),
        asignarA("d", 5))),
    porCada(lista([1, 2, 3, 5, 6]), (sumarA("x", 1),)),
    devolver("x")
), como="función compleja")

ejecutar("función compleja")
```