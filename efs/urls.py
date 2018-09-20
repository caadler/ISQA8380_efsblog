from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('password_change/',
         views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^password_reset_form/$', views.password_reset, name='password_reset_form'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),


]
