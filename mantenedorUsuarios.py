


import json
from datetime import datetime


JSON_FILE = 'usuarios.json'

def cargar_usuarios():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = []
    return usuarios

def guardar_usuarios(usuarios):
    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4)

def agregar_usuario(nombre, email):
    usuarios = cargar_usuarios()
    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': nombre,
        'email': email,
        'fecha_registro': datetime.now().isoformat(),
    }
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

def editar_usuario(id_usuario, nombre=None, email=None):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            if nombre:
                usuario['nombre'] = nombre
            if email:
                usuario['email'] = email
            guardar_usuarios(usuarios)
            return True
    return False  

def eliminar_usuario(id_usuario):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            return True
    return False  

def buscar_usuario(id_usuario):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            return usuario
    return None  



   
