import requests
from API.metodo_http import obtener_publicaciones

URL = "https://jsonplaceholder.typicode.com/posts"

res = requests.get(URL)
# print (res.json())

# ## POST JSON
# datos = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }   

# res = requests.post(URL, json=datos)
# print (res.json())

# ## Login DummyJSON
# resp = requests.post(
#     "https://dummyjson.com/auth/login", 
#     headers={"Content-Type":"application/json"},
#     json={
#         "username":"kminchelle",
#         "password":"0lelplR",
#         "expiresInMins":30
#         })

# ## Con API Key
# api_key = "YOUR_API_KEY"
# url = "https://reqres.in/api/users"

# headers = {
#     "x-api-key": api_key,
# }

# respuesta_get = requests.get(url, headers=headers)
# print(respuesta_get.json())

# ## Prueba de API DummyJSON
# urlDummy = "https://dummyjson.com/products"
# print("\nLista de productos:")

# respuesta_get = requests.get(urlDummy)
# print("Codigo HTTP:", respuesta_get.status_code)

# productos = respuesta_get.json()

# indice_max = len(productos["products"])
# print("Cantidad de productos:", indice_max)

# nuevo_producto = {
#     "title": "Nuevo Producto",
#     "description": "Descripción del nuevo producto",
#     "price": 99.99,
#     "brand": "Marca Ejemplo",
#     "category": "Categoría Ejemplo"
# }

# respuesta_post = requests.post(f"{urlDummy}/add", json=nuevo_producto)
# print("Código HTTP:", respuesta_post.status_code)
# producto_creado = respuesta_post.json()


# resp_get_final = requests.get(urlDummy)
# print("Código HTTP:", resp_get_final.status_code)

# datos_finales = resp_get_final.json()
# productos_finales = datos_finales["products"]
# productos_finales.append(producto_creado)

# print("Productos finales después de agregar el nuevo producto:")
# print(len(productos_finales))

datos_actualizados = {
    "title": "foo actualizado",
    "body": "bar actualizado",
    "userId": 1
}

res = requests.put(f"{URL}/1", json=datos_actualizados)

print("Código HTTP:", res.status_code)
print("Datos actualizados:", res.json())

res = requests.delete(f"{URL}/1")
print("Código HTTP:", res.status_code)  
