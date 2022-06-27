from django.urls import path,include
from .views import home, productos, index, seguimiento, donacion, contacto, seguido, Productolista, adm, crearpro, iniciosesion
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('index' , index, name="index"),
    path('productos', productos, name="productos"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('donacion', donacion, name="donacion"),
    path('contacto', contacto, name="contacto"),
    path('seguido', seguido, name="seguido"),
    path('Productolista', Productolista, name="Productolista"),
    path('adm', adm, name="adm"),
    path('crearpro', crearpro, name="crearpro"),
    path('iniciosesion', iniciosesion, name="iniciosesion"),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="InicioSeccion")),
    path('logout', LogoutView.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)