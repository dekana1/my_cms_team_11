from django.urls import path

from . import views

app_name = 'webella'


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('on-boarding/', views.on_boarding, name='on_boarding'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('pdashboard/', views.portfolio_dashboard, name='portfolio_dashboard'),

]