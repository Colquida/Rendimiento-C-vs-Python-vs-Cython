'''
-+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-  
==================================================================================
-+-   -+-   -+-       :::::| :::::| :::::| :::::| :::::|  -+-   -+-   -+-
-+-   -+-   -+-       :::::| :::::| :::::| :::::| :::::| 	-+-   -+-   -+-
===============  						                                   ===============
===============  	    Calculador de números primos en C   ===============
===============		  	          27/04/2021			               ===============
=============== 		              Autores			                =============== 
===============							                                    =============== 
===============	  	    Rubén Alexis Núñez Montaña		       =============== 
===============       Jonathan Alexander Torres Benítez		 ===============  
=============== 						                                    =============== 
===============	  	  ruben.nunez01@correo.usa.edu.co		    ===============
===============		  jonathana.torres@correo.usa.edu.co	    ===============
===============							                                    ===============
===============	  	   Universidad Sergio Arboleda		       =============== 
===============							                                    =============== 
=============== 		           Presentado a:			             =============== 
===============	  	      John Jairo Corredor, PhD.		      =============== 
===============		  Computación Paralela y Distribuida	    =============== 
-+-   -+-   -+-      :::::| :::::| :::::| :::::| :::::| 	-+-   -+-   -+-
-+-   -+-   -+-      :::::| :::::| :::::| :::::| :::::| 	-+-   -+-   -+-
================================================================================== 
 -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-   -+-  
 '''

#!/usr/bin/env python
def primes_python(nb_primes):
    p = []
    n = 2
    while len(p) < nb_primes:
        # ¿Es n un número primo?
        for i in p:
            if n % i == 0:
                break

        # Si el break no pasa en el loop
        else:
            p.append(n)
        n += 1
    return p
