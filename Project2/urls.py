from django.contrib import admin
from django.urls import path
from addapp import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('addapp',views.input),
    path('add',views.add),
]

