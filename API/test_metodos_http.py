import pytest
from pytest_check import check
from API.metodo_http import(obtener_publicaciones,
                            obtener_publicacion_por_id,
                            crear_publicacion,
                            obtener_usuarios,
                            obtener_usuario_por_id
                            )

BASE = 'http://jsonplaceholder.typicode.com'

@pytest.fixture()
def post_url():
    return f"{BASE}/posts"

@pytest.fixture()
def user_url():
    return f"{BASE}/users"
   
def test_obtener_publicaciones(post_url):
    publicaciones = obtener_publicaciones(post_url)
    assert publicaciones.status_code == 200
    assert isinstance(publicaciones.json(), list)
    assert len(publicaciones.json()) > 0

    for publicacion in publicaciones.json():
        assert 'userId' in publicacion
        assert 'id' in publicacion
        assert 'title' in publicacion
        assert 'body' in publicacion

# def test_obtener_publicacion_por_id(post_url):
#     id_publicacion = 1
#     publicacion = obtener_publicacion_por_id(post_url, id_publicacion)
#     assert isinstance(publicacion, dict)
#     assert publicacion['id'] == id_publicacion

# def test_crear_publicacion(post_url):
#     datos = {
#         "title": "foo",
#         "body": "bar",
#         "userId": 1
#     }
#     nueva_publicacion = crear_publicacion(post_url, datos)
#     assert isinstance(nueva_publicacion, dict)
#     assert nueva_publicacion['title'] == datos['title']
#     assert nueva_publicacion['body'] == datos['body']
#     assert nueva_publicacion['userId'] == datos['userId']

## Check sirve para hacer multiples assert sin que se detenga el test al primer error
def test_obtener_usuarios(user_url):
    respuesta = obtener_usuarios(user_url)
    datos = respuesta.json()
    check.equal (respuesta.status_code, 200)
    check.is_true(isinstance(datos, list))
    check.is_true(len(datos) > 0)

    for usuario in datos:
        check.is_true('id' in usuario, f"El usuario {usuario} no tiene el campo 'id'")
        check.is_true('name' in usuario, f"El usuario {usuario} no tiene el campo 'name'")
        check.is_true('email' in usuario, f"El usuario {usuario} no tiene el campo 'email'")



@pytest.mark.parametrize("campo, esperado, mensaje_error", [
    ("name", "Leanne Graham", "El nombre del usuario no es 'Leanne Graham'"),
    ("email", "Sincere@april.biz", "El email del usuario no es 'Sincere@april.biz'"),
    ("address.city", "Gwenborough", "La ciudad del usuario no es 'Gwenborough'"),
    ("username", "Bret", "El nombre de usuario no es 'Bret'")
])
def test_obtener_usuarios_por_id(user_url, campo, esperado, mensaje_error):
    id_usuario = 1
    usuario = obtener_usuario_por_id(user_url, id_usuario)
    assert usuario.status_code == 200
    
    datos = usuario.json()
    check.is_true(isinstance(datos, dict))
    check.equal(datos['id'], id_usuario)    

    valor = datos
    partes = campo.split('.')
    for parte in partes:
        valor = valor[parte]

    check.equal(valor, esperado, mensaje_error)
