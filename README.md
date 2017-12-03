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
    sumar("x", -5),
), como="restar")

definir((
    crear("x"),
    asignar("x", parametro("a")),
    sumar("x", 5),
    usar("restar"),
    si(esigual(6, 5),
        (crear("z"),
        asignar("z", 5)),
    sino=(crear("d"),
        asignar("d", 5))),
    porCada(lista([1, 2, 3, 5, 6]), (sumar("x", 1),)),
    devolver("x")
), como="función compleja")

ejecutar("función compleja", {"a": 5})
```