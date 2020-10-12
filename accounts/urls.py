from django.urls import path 

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('upload',views.shop_image_view,name='postUpload'),
    path('success', views.success, name = 'success'),
    path('shop_images', views.display_shop_images, name = 'shop_images'), 
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)