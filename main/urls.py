from django.urls import path
from main import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('moments/',views.moments,name='moments'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('service-details/<uuid:id>/',views.service_details,name='service_details'),
    path('all-courses/',views.all_courses,name="all-courses"),
    path('university-detail/<uuid:id>/',views.university_detail_page,name='university_detail_page'),
    path('ajax/load-universities/', views.load_univeristies, name='load_univeristies'), 
    path('ajax/load-courses/', views.load_courses, name='load_courses'), 
]
