from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # path for home page
    path('',views.index,name='index'),
    # path for registration page
    path('register',views.register,name='register'),
    # path for login page
    path('login',views.login,name='login'),
    # path for loging out
    path('logout',views.logout,name='logout'),
    # path for uploading product page
    path('upload',views.upload_post,name='postUpload'),
    # path for HttpResponse "Success"
    path('success', views.success, name = 'success'),
    # path for showing all products page
    path('community_page', views.community_page, name = 'community_page'), 
    # path for showing all products page
    path('categories_page', views.category_page, name = 'category_page'),
    # path for proile update page
    path('update', views.profile,name='profile'),
    # path for category wise products
    path('product_category', views.product_category,name='product_category')

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)