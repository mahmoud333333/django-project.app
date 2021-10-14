from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

   path('register/', views.registerPage, name="register"),
	 path('login/', views.loginPage, name="login"),  
	 path('logout/', views.logoutUser, name="logout"),



    path('', views.home,name="home"),
    path('user/', views.userPage, name="user-page"),
    path('whse/', views.whse, name="whse"),
    path('staff/<str:pk_test>/', views.staff, name="staff"),
    path('status/', views.Status, name="status"),
    
    
    path('create_tasks/', views.createTASKS, name="create_tasks"),
    path('update_tasks/<str:pk>/', views.updateTASKS, name="update_tasks"),
    path('delete_tasks/<str:pk>/', views.deleteTASKS, name="delete_tasks"),
    path('confirmed_tasks/<str:pk>/', views.confirmedTASKS, name="confirmed_tasks"),
   
    
     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="product/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="product/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="product/password_reset_form.html"), 
     name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="product/password_reset_done.html"), 
        name="password_reset_complete"),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)