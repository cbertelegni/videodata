video-data
==========

## Descripción de la APP

Esta aplicación sirve para generar datos en videos, es decir, marcas en el tiempo asociadas al contenido. Estas marcas son para taguear personas, hechos, fechas, lugares, etc, a estas marcas se podrá agregar textos descriptivos que enriquezcan esa marca.

* Cualquier usuario podrá acceder al punto de su interés en el video buscando por los textos ingresados.

* Constará de un buscador para traer el video de interés, buscará todas las coincidencias en los portales de video más importantes (youtube, vimeo, etc.) También tendrá un imputText donde se podrá ingresar directamente el link. En el caso de buscar un video por tema aparecerá un listado en el cual se podrá seleccionar uno para comenzar la edición. 

* La pantalla tendrá un reproductor de video con un controlador de tiempo con el cual se podrá agregar una marca en un momento específico, y esa marca tendrá la descripción ("quién", "qué", "cómo" FLOR!) 

* Tendrá la posibilidad de dibujar/agregar gráficos (flechas, círculos) o fotos. Se podrá ubicarlas en un lugar específico de la pantalla, tendrán una duración acotada, y un tamaño limitado
Esas marcas tendrán un in y un out de tiempo.

* Las marca aparecerán en el timeline del video, al pasar el cursor mostrará un tooltip con los datos ingresados: un título, descripción, un link. A los textos se les podrá dar estilo (negrita, itálica, color para la marca, los mismos aparecerán como referencias) 

* Cada video que se ingrese alimenta la base de datos, la cual luego se va a poder consultar por persona, tema o texto libre.

* Posibilidad de compartir el video (facebook, twitter, google plus) desde una marca específica
* LogIn with socialmedia

## Páginas

Home:
1. listado de últimos videos cargados, buscador, compartir
2. liberá tu video
3. Editor de video: reproductor de video, timeline con editor de texto, modificar marca
4. Pantalla resultado de búsqueda: reproductor cargado con el video seleccionado, con las marcas de la palabra buscada resaltada. Denunciar contenido
