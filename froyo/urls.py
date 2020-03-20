from django.urls import path

from .views import froyo
from .views import ingredients
from .views import ingredients_list
from .views import ingredients_detail
from .views import ingredients_update
from .views import ingredients_create
from .views import recipes
from .views import recipes_list
from .views import recipes_detail
from .views import recipes_update
from .views import recipes_create
from .views import orders
from .views import orders_list
from .views import orders_detail
from .views import orders_update
from .views import orders_create

urlpatterns = [
    path('froyo', froyo),
    path('froyo/ingredients', ingredients),
    path('froyo/ingredients/list', ingredients_list),
    path('froyo/ingredients/detail', ingredients_detail),
    path('froyo/ingredients/update', ingredients_update),
    path('froyo/ingredients/create', ingredients_create),
    
    path('froyo/recipes', recipes),
    path('froyo/recipes/list', recipes_list),
    path('froyo/recipes/detail', recipes_detail),
    path('froyo/recipes/update', recipes_update),
    path('froyo/recipes/create', recipes_create),
    
    path('froyo/orders', orders),
    path('froyo/orders/list', orders_list),
    path('froyo/orders/detail', orders_detail),
    path('froyo/orders/update', orders_update),
    path('froyo/orders/create', orders_create),
    
]
