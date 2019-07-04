from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('home', views.home, name='home'),
    path('rsvp/<int:user_id>/', views.rsvp, name='rsvp'),
    path('make_comment', views.make_comment, name='make_comment'),
    path('rsvp/send_answer/<int:user_id>', views.send_answer, name='send_answer'),
    path('rsvp/show_answer/<int:user_id>/', views.show_answer, name='show_answer'),
    path('rsvp/answer/plus_one/<int:user_id>/', views.plus_one_form, name='plus_one'),
    path('rsvp/answer/plus_one_info/<int:user_id>/', views.plus_one_info, name='plus_one_info'),
]