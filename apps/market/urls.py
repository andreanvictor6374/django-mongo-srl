from django.urls import path


from . import views

app_name = 'market'

urlpatterns = [
    path('', views.product_all, name='store_home'),

]