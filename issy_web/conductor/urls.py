
from django.conf.urls import url
from conductor import views


urlpatterns = [
url(r'^conductor/$',views.AlquilarAuto.as_view(),name="alquilar_auto"),
url(r'^conductor/lista_autos$',views.alquilar_auto_lista,name="lista_autos"),
url(r'^conductor/conductor_info$',views.ConductorInfo.as_view(),name="conductor_info"),
url(r'^$',views.AlquilarAuto.as_view(),name="alquilar_auto"),

]