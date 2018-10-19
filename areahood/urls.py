from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'profile/$',views.create_profile_view,name='profile'),
    url(r'^$', views.display, name='display'),
    url(r'^insta/$', views.create_post_view, name='post'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)