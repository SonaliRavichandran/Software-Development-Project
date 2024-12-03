from django.urls import path
from .import views

urlpatterns=[
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_view,name="login"),
    path('forgetpassword',views.forgetpassword,name="forgetpassword"),
    path('events',views.events,name="events"),
    path('anirudh',views.anirudh,name="anirudh"),
    path('yuvan',views.yuvan,name="yuvan"),
    path('harris',views.harris,name="harris"),
    path('arrahman',views.arrahman,name="arrahman"),
    path('booktickets', views.book_event, name='bookticket'),
    path('payment', views.book_ticket, name='book_ticket'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback/', views.feedback, name='feedback'), 
    path('Newsletter/', views.subscribe, name='Newsletter'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contactus',views.contactus,name="contactus"),
    path('book-event/', views.book_event, name='book_event'),
    path('process-payment/', views.process_payment, name='payment'),
    path('create-event/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('search/', views.search_events, name='search_events'),
    path('book/<int:event_id>/', views.book_ticket, name='book_ticket'),
     path('search-result/', views.search_events, name='search_events'),
    path('book/<int:event_id>/', views.book_ticket, name='book_ticket'),

]