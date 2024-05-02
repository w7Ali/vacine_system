from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.hospital, name='hospitals'),
    path('patient/', views.add_patient, name="add_patient")

]

city_urls = [

    # City URLs
    path('cities/', views.city_list, name='city_list'),
    path('cities/<int:pk>/', views.city_detail, name='city_detail'),
    path('cities/create/', views.city_create, name='city_create'),
    path('cities/<int:pk>/update/', views.city_update, name='city_update'),
    path('cities/<int:pk>/delete/', views.city_delete, name='city_delete'),
    path('cities_json/', views.city_list_json, name='json_city'),
]
hospital_urls = [
    # Hospital URLs
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('hospitals/<int:pk>/', views.hospital_detail, name='hospital_detail'),
    path('hospitals/create/', views.hospital_create, name='hospital_create'),
    path('hospitals/<int:pk>/update/', views.hospital_update, name='hospital_update'),
    path('hospitals/<int:pk>/delete/', views.hospital_delete, name='hospital_delete'),
    path('hospitals_json/<str:city>', views.hospital_list_json, name='json_hospitals')
]

urlpatterns += city_urls + hospital_urls
