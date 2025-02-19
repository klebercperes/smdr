from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', accounts_views.login_view, name='login'),
    path('accounts/signup/', accounts_views.signup_view, name='signup'),
    path('accounts/logout/', accounts_views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]