#!/usr/bin/env python
# coding: utf-8

# In[96]:


try:
    pollo = int(input('¿Qué pollo quiere cocinar? (máximo 4 pollos y 16 Kg)'
                      '\n\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
except ValueError:
    pollo = int(input('No se eligió un valor válido...'
                      '\n¿Qué pollo quiere cocinar? (máximo 4 pollos y 16 Kg)'
                      '\n\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
cantidad = 0
suma_peso = []
cantidad_de_agua = 15
while cantidad < 4 and sum(suma_peso) < 16:
    try:
        if pollo == 1:
            cantidad += 1
            suma_peso.append(4)
            sum(suma_peso)
            pollo = int(input(f'Eligió pollo pequeño, '
                              f'hay {cantidad} pollos (max 4) y {str(sum(suma_peso))} Kg (max 16 Kg) en el horno'
                              '\n¿Quiere cocinar otro?'
                              '\n\n-0 Detener\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
        elif pollo == 2:
            cantidad += 1
            suma_peso.append(6)
            sum(suma_peso)
            pollo = int(input(f'Eligió pollo mediano, '
                              f'hay {cantidad} pollos (max 4) y {str(sum(suma_peso))} Kg (max 16 Kg) en el horno'
                              '\n¿Quiere cocinar otro?'
                              '\n\n-0 Detener\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
        elif pollo == 3:
            cantidad += 1
            suma_peso.append(8)
            sum(suma_peso)
            pollo = int(input(f'Eligió pollo grande, '
                              f'hay {cantidad} pollos (max 4) y {str(sum(suma_peso))} Kg (max 16 Kg) en el horno'
                              '\n¿Quiere cocinar otro?'
                              '\n\n-0 Detener\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
        elif pollo == 0:
            print(f'Muy bien, cocinando {cantidad} pollos...'
                  f'\nSe cocinaron {str(sum(suma_peso))} Kg de pollo')
            break
        else:
            pollo = int(input('No se eligió un valor válido...'
                              f'\nHay {cantidad} pollos (max 4) y {str(sum(suma_peso))} Kg (max 16 Kg) en el horno'
                              '\n¿Quiere cocinar otro?'
                              '\n\n-0 Detener\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
        if cantidad >= 4:
            print('Cantidad máxima de pollo alcanzada, cocinando 4 pollos...'
                  f'\nSe cocinaron {str(sum(suma_peso))} Kg de pollo')
            break
        elif sum(suma_peso) >= 16:
            print(f'Límite de peso alcanzado (16 Kg), cocinando {cantidad} pollos...')
            break
    except ValueError:
        pollo = int(input('No se eligió un valor válido...'
                          f'\nHay {cantidad} pollos (max 4) y {str(sum(suma_peso))} Kg (max 16 Kg) en el horno'
                          '\n¿Quiere cocinar otro?'
                          '\n\n-0 Detener\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
tiempo = cantidad
if tiempo <= 2:
    tiempo = "60 minutos"
    print ("****EL tiempo para cocinarse es de:",tiempo)
else:
    tiempo = "90 minutos"
    print ("****EL tiempo para cocinarse es de:",tiempo)
if tiempo == "60 minutos":
    cantidad_de_agua = 15 / 2 
    print ("****La cantidad de agua que quedo es:", cantidad_de_agua,"Litros")
else:
    cantidad_de_agua = 15 / 4
    print ("****La cantidad de agua que quedo es:", cantidad_de_agua,"Litros")
vueltas = 5
if tiempo == "60 minutos":
    vueltas = 5 * 60
    print("****Las vueltas realizadas son:",vueltas)
else:
    vueltas = 5 * 90
    print("****Las vueltas realizadas son:",vueltas)


# In[60]:


pollo = int(input('¿Qué pollo quiere cocinar? (máximo 4 pollos y 16 Kg)'
                     '\n\n-1 Pequeño (4 kg)\n-2 Mediano (6 kg)\n-3 Grande (8 kg)\n'))
suma_peso = []
if pollo == 1:
       suma_peso.append(4)
       print(suma_peso )
elif pollo == 2:
   suma_peso.append(6)
   print(suma_peso)
elif pollo == 3:
   suma_peso.append(8)
   print(suma_peso)
tiempo = suma_peso
def tiempo_cocinar(tiempo):
   if tiempo == [4] :
       tiempo = "nada"
       print("su tiempo es:", tiempo)
   if tiempo == [6]:
       tiempo = "Nose"
       print("su tiempo es:",tiempo)
   else:
       tiempo = "sapo"
       print("su tiempo es:",tiempo)
print(tiempo_cocinar(tiempo))
       


# In[58]:


lista_tiempo= [4,6,8,10,12,14,16]
pollo = int(input("numero "))
tiempo = suma_peso
suma_peso = []
if pollo == 1:
    suma_peso.append(4)
    print(suma_peso )
elif pollo == 2:
    suma_peso.append(6)
    print(suma_peso)
if tiempo == [4]:
    tiempo = "sapo"
    print (tiempo)
elif teimpo == [6]:
    teimpo = "hola"
    print(tiempo)
else:
    tiempo = "nada"
    print(tiempo)


    


# In[84]:





# In[ ]:


if tiempo == [4]:
    tiempo = "60 minutos"
    print("su tiempo es:", tiempo)
elif tiempo == [6]:
    tiempo = "90 minutos"
    print("su tiempo es:", tiempo)
elif tiempo == [8]:
    tiempo = "10 minutos"
    print("su tiempo es:", tiempo)
elif tiempo == [10]:
    tiempo = "20 minutos"
    print("su tiempo es:", tiempo)
else:
    tiempo = "80 minutos"
    print("su tiempo es:", tiempo)

