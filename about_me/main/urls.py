from django.urls import path, include

from .views import index, detail

app_name = 'main'


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:employee_id>/', detail, name='detail')
]
