import instaloader

def obtener_comentarios(url_publicacion, usuario=None, contraseña=None):
    # Crea una instancia de Instaloader
    loader = instaloader.Instaloader()

    # Si se proporcionan credenciales de inicio de sesión, inicia sesión en Instagram
    if usuario and contraseña:
        loader.login(usuario, contraseña)

    # Obtén la publicación
    post = instaloader.Post.from_shortcode(loader.context, url_publicacion.split('/')[-2])

    # Lista para almacenar los comentarios
    comentarios = []

    # Itera sobre los comentarios de la publicación
    for comment in post.get_comments():
        try:
            # Decodifica el texto del comentario para manejar caracteres especiales
            decoded_text = comment.text.encode('cp1252', errors='replace').decode('cp1252')
            comentarios.append(decoded_text)
        except UnicodeEncodeError:
            # En caso de error de codificación, agrega el texto original reemplazando los caracteres problemáticos
            comentarios.append(comment.text.encode('cp1252', errors='replace').decode('cp1252'))

    return comentarios
#final_comentarios = obtener_comentarios("https://www.instagram.com/p/C51wNPMu3br/", "juanadolfo365", "oaxaca123")
from instascrape import *

def obtener_ultimos_posts_instagram(username, password, target_username, cantidad=10):
    final_array = []
    # Crear una instancia de Instaloader y autenticarse
    L = instaloader.Instaloader()
    L.login(username, password)

    try:
        # Obtener el perfil de Instagram
        profile = instaloader.Profile.from_username(L.context, target_username)

        # Obtener los últimos posts
        posts = profile.get_posts()

        # Iterar sobre los últimos posts e imprimir los enlaces
        for i, post in enumerate(posts):
            if i >= cantidad:
                break
            post_url = f"https://www.instagram.com/p/{post.shortcode}/"
            final_array.append(post_url)

    except instaloader.exceptions.ProfileNotExistsException:
        final_array.append("El perfil especificado no existe")

    return final_array

array_heybanco = []
array_getpost = obtener_ultimos_posts_instagram("pidabi6890", "hola123", "heybanco", cantidad=10)
for links in array_getpost:
  final_comentarios = obtener_comentarios(links, "pidabi6890", "hola123")
  for comentario in final_comentarios:
    array_heybanco.append(comentario)

print(array_heybanco)