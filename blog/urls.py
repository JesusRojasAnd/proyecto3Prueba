from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name="inicio"),
    path('blog',listado,name="blog"),
    path('entrada/crear',crea_entrada,name="crea_entrada"),
    path('categoria/crear',crea_categoria,name="crea_categorias"),
    path('blog/categorias',listadoCategorias,name="blogCategoria"),
]