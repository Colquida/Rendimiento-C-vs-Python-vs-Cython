# Rendimiento-C-vs-Python-vs-Cython

Contiene el programa de hallazgo de números primos a través en su versión de C, Python y posteriormente Cython

Para compilar el programa primes_c.c, lo puede hacer de la forma tradicional gcc -o nombreEjecutable primes_c.c
De momento para revisar el tiempo de ejecución realice: time ./nombreEjecutable #inicio #fin

Para verificar el funcionamiento del programa primes_python.py se recomienda instalar ipython3:
El comando para hacerlo es sudo apt install ipython3

Una vez instalado, podrá probar el programa de la siguiente forma ejecutando en consola:
ipython3 --no-banner

Esto le permitirá acceder a una línea de comandos especial que le dejará llamar el programa. A continuación, debe escribir:

import primes_python
primes_python.primes_python(#númerodeseado)

Y en consola podrá ver la lista de números primos de acuerdo al número deseado.
Para ver el tiempo use lo siguiente:

python3 -m timeit -s 'from primes_python import primes_python' 'primes_python(#deseado)'

