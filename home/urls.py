from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='electronic-index'),
    path('<int:styles>/',views.get_styles_by_number),
    path('<str:styles>/',views.get_styles, name='electronic-style'),

]