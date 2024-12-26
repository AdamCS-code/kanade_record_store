from django.urls import path
from authentication.views import login, register, create_product_flutter, logout, show_json

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('logout/', logout, name='logout'),
    path('show_json/', show_json),
]
