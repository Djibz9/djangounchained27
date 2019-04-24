from django.urls import path

from . import views
'''In here you can that a second page was added to the newpage section. A page within a page.'''
urlpatterns = [
    path('page2', views.page2, name='page2'),
    path('', views.index, name='index'),
]