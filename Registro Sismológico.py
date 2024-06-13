import csv
import random
import time

palabra = "....."



datos = [
    ['Region', 'Zonas'],
    ['Tarapaca', 'Norte'],
    ['Antofagasta', 'Norte'],
    ['Atacama', 'Norte'],
    ['Maule', 'Centro'],
    ['Valparaiso', 'Centro'],
    ['Los Rios', 'Sur'],
    ['Ñuble', 'Sur']  
]


with open('Zonas.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)


    
ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona1_to = [ra_1, ra_2, ra_3]

zona_max1 = max(zona1_to)

ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona2_to = [ra_1, ra_2, ra_3]

zona_max2 = max(zona2_to)

ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona3_to = [ra_1, ra_2, ra_3]

zona_max3 = max(zona3_to)


ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona4_to = [ra_1, ra_2, ra_3]

zona_max4 = max(zona4_to)

ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona5_to = [ra_1, ra_2, ra_3]

zona_max5 = max(zona5_to)

ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona6_to = [ra_1, ra_2, ra_3]

zona_max6 = max(zona6_to)

ra_1 = random.randint(1,10)
ra_2 = random.randint(1,10)
ra_3 = random.randint(1,10)

zona7_to = [ra_1, ra_2, ra_3]

zona_max7 = max(zona7_to)


while True:

    print("\n menu")
    print("seleccione una zona")
    print("1-Norte")
    print("2-Centro")
    print("3-Sur")
    print("4-Salir")
    opc = input("elija entre (1-4):"+ '')
    print()
    if opc =="1":
        print("seleccione la region de la zona Norte:")

        print("1-Tarapaca")
        print("2-Antofagasta")
        print('3-Atacama')
        opc=input("elija:" + '')
        if opc =='1':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            print("se dectecto un sismo de", zona1_to, 'en Tarapaca')
            print()
        if opc =='2':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            
            print("se dectecto un sismo de", zona2_to, 'en Antofagasta')
            print()
        if opc =='3':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            print("se dectecto un sismo de", zona3_to, 'en Atacama')
            
    elif opc =="2":
        print("seleccione la region de su zona centro:")

        print("1-Maule ")
        print("2-Valparaiso")
        opc=input("elija:" + '')
        if opc =='1':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            print("se dectecto un sismo de", zona4_to, 'en Maule')
            print()
        if opc =='2':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            print("se dectecto un sismo de", zona5_to, 'en Valparaiso')
            print()
        
    elif opc =="3":
        print("seleccione la region de su zona centro:")

        print("1-Los rios ")
        print("2-Ñuble")
        opc=input("elija:" + '')
        if opc =='1':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            print("se dectecto un sismo de", zona6_to, 'en Los Rios')
            print()
        if opc =='2':
            print(opc)
            print("se detecto sismo.")
            print("Ingresando en escala de Richter")
            for letra in palabra:
                print(letra, end='', flush=True)
                time.sleep(0.5)
            print()
            print("se dectecto un sismo de", zona7_to, 'en Ñuble')
            print()
        
    else:
        opc=='4'
        break
    
print("Registro de la mayor intensidad de zonas:")

print("")

Max = [
    ['Region', 'Zonas'],
    ['Tarapaca', f'Zona Norte con una intensidad de {zona_max1}'],
    ['Antofagasta', f'ZonaNorte con una intensidad de {zona_max2}'],
    ['Atacama', f'Zona Norte con una intensidad de {zona_max3}'],
    ['Maule', f'Zona Centro con una intensidad de {zona_max4}'],
    ['Valparaiso', f'Zona Centro con una intensidad de {zona_max5}'],
    ['Los Rios', f'Zona Sur con una intensidad de {zona_max6}'],
    ['Ñuble', f'Zona Sur con una intensidad de {zona_max7}']
]        
for row in Max:
    print(row)