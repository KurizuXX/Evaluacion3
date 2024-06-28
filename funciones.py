import json

def add_cat():
    Nombre_Cat=input('Ingrese catergoria a agregar: ')
    with open('biblioteca.json', 'r') as file:
        data=json.load(file)
    data['Categoria'].append({
        'CategoriaID' : len(data['Categoria'])+1,
        'Nombre' : Nombre_Cat
    }) 
    with open('biblioteca.json', 'w') as file:
        json.dump(data, file, indent=4)
        print('categoria agregada correctamente')


def edit_cat():
    with open('biblioteca.json', 'r') as file:
        data=json.load(file)
        cat_edit=int(input('ingrese el ID de la categoria a editar: '))
        for categorias in data['Categoria']:
            if categorias['CategoriaID'] == cat_edit:
                categorias['Nombre'] = input('Ingrese nuevo nombre de categoria: ')
        with open('biblioteca.json', 'w') as file:
            json.dump(data, file, indent=4)
            print('categoria editada correctamente')


def del_cat():
    with open('biblioteca.json', 'r') as file:
        data=json.load(file)
        del_cat=int(input('Ingrese el ID de la categoria a eliminar: '))
        for categorias in data['Categoria']:
            if categorias['CategoriaID'] == del_cat:
                data['Categoria'].remove(categorias)
                print('se elimino la categoria',categorias['Nombre'],'\n'),input()
        with open('biblioteca.json', 'w') as file:
            json.dump(data, file, indent=4)
            print('categoria eliminada correctamente')

def search_cat():
    with open('biblioteca.json', 'r') as file:
        data=json.load(file)
        search_cat=int(input('Ingrese el ID de la categoria a buscar: '))
        for categorias in data['Categoria']:
            if ['CategoriaID'] == search_cat:
                print('ID: ',categorias['CategoriaID'])
                print('Nombre: ',categorias['Nombre'])
                input('presiona enter para continuar')






















