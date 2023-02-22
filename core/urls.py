from django.urls import path
from django.contrib.auth import views as auth_views
from .views import frontpage, mail_letter, loginView, search, detailPage

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('create/', mail_letter, name="mail_letter"),
    path('search/', search, name='search'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('<slug:slug>/', detailPage, name='detail'),
]