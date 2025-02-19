from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from files import views as files_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', accounts_views.login_view, name='login'),
    path('accounts/signup/', accounts_views.signup_view, name='signup'),
    path('accounts/logout/', accounts_views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('upload/', files_views.upload_file, name='upload_file'),
    path('upload_customers_csv/', files_views.upload_customers_csv, name='upload_customers_csv'),
    path('view_uploaded_file/<str:filename>/', files_views.view_uploaded_file, name='view_uploaded_file'),
    path('', files_views.dashboard, name='dashboard'),
]
