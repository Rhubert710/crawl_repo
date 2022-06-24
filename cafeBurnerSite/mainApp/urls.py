from django.urls import path

from . import views

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
    
]