from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include ('main.urls')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='logout'),
    url(r'^signup/$', TemplateView.as_view(template_name="main/auth.html"), name='signup'),
    url(r'^email-verification/$', TemplateView.as_view(template_name="account/email_verification.html"), name='email-verification'),
    url(r'^password-reset/$', TemplateView.as_view(template_name="account/password_reset.html"), name='password-reset'),
    url(r'^password-reset/confirm/$', TemplateView.as_view(template_name="account/password_reset_confirm.html"), name='password-reset-confirm'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^password-change/$', TemplateView.as_view(template_name="account/password_change.html"), name='password-change'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^chat/', include('chat.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
