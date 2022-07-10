from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('index2', views.index2, name='index2'),
    path('uploadImage', views.uploadImage, name='uploadImage'),
    path('uploadImage/<error>', views.uploadImage, name='uploadImage'),
    path('saveImage/', views.saveImage, name='saveImage'),
    path('newFlyerFormMobile/<imgPk>', views.newFlyerFormMobile, name='newFlyerFormMobile'),
    path('saveFlyerMobile/', views.saveFlyerMobile, name='saveFlyerMobile'),
    path('saveFlyerDesktop/', views.saveFlyerDesktop, name='saveFlyerDesktop'),
    # path('flyerSubmitted', views.flyerSubmitted, name='flyerSubmitted'),
    path('watchList', views.watchList, name='watchList'),
    path('data', views.data, name='data'),
    path('promote', views.promote, name='promote'),
    path('about', views.about, name='about'),
    path('uploadMultiple', views.uploadMultiple, name='uploadMultiple'),
    path('saveMultiple', views.saveMultiple, name='saveMultiple'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    
]