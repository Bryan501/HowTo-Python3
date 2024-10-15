"""
-------------------------------------------------
        GENERADOR DE CONTRASEÑAS SEGURAS
-------------------------------------------------
Descripción:
  Este programa genera una contraseña segura de acuerdo
  a los siguientes criterios:
  
  - Debe incluir al menos una letra mayúscula.
  - Debe incluir al menos una letra minúscula.
  - Debe incluir al menos un número.
  - Debe incluir al menos un símbolo especial. ( !@#$%^&*() )
  
  El usuario puede definir la longitud de la contraseña
  (mínimo 8 caracteres) y el programa devolverá una
  contraseña generada aleatoriamente que cumpla con los
  requisitos de seguridad.

Instrucciones:
  1. Ingresa la longitud deseada de la contraseña.
  2. El programa generará una contraseña aleatoria.
  3. Podrás elegir si deseas generar otra contraseña.
-------------------------------------------------

-------------------------------------------------
                EJEMPLO DE EJECUCIÓN
-------------------------------------------------


Ingrese la longitud de la contraseña: 12
Tu nueva contraseña segura es: H8$jCz4Lp&!
¿Deseas generar otra contraseña? (s/n): n
"""

import random, string, time

def gen_passwd():
    while True:  
        try:
            passwd1 = int(input("Ingrese la longitud de la contraseña (mínimo 8): ")) 
            if passwd1 >= 8:
                break  
            else:
                print("ERROR: La longitud debe ser al menos 8.")
        except ValueError:
            print("ERROR: Por favor, ingrese un número entero válido.")  

    minuscula = string.ascii_lowercase
    mayuscula = string.ascii_uppercase
    puntuacion = string.punctuation
    num = string.digits

    char = minuscula + mayuscula + puntuacion + num

    passwd = ""

    for _ in range(passwd1):
        passwd += random.choice(char) 

    print("Tu nueva contraseña segura es:", passwd)
    
    time.sleep(5) 
    again = input("¿Deseas generar otra contraseña? (s/n): ") 
    
    if again.lower() == "s":  
        return gen_passwd()  
    
    else:
        pass  

gen_passwd()



