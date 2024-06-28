import json
import os, time
import menus 
import funciones

with open('biblioteca.json', 'r') as file:
    data = json.load(file)
while True:
    menus.mostrar_menu_inicial()
    opc=int(input('digite su seleccion: '))
    os.system('cls')
    time.sleep(1)
    if opc == 1:
        while True:
            menus.menu_mantenedores()
            opc_mantenedores=int(input('digite su seleccion: '))
            os.system('cls')
            time.sleep(1)
            if opc_mantenedores ==1:
                funciones.add_cat()
                time.sleep(1)
                os.system('cls')
                continue
            elif opc_mantenedores ==2:
                funciones.edit_cat()
                time.sleep(1)
                os.system('cls')
                continue
            elif opc_mantenedores == 3:
                funciones.del_cat()
                time.sleep(1)
                os.system('cls')
                continue
            elif opc_mantenedores ==4:
                funciones.search_cat()
                time.sleep(1)
                os.system('cls')
            elif opc_mantenedores ==5:
                break
    elif opc ==2:
        print('reportes')

    elif opc == 3:
        break
    
    

    
