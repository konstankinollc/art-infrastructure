from django.conf.urls import url

from lighting.api.v1 import views as views_v1

urlpatterns = [

    url(r'^v1/bacnet_lights/$', views_v1.BACNetViewSet.as_view(), name='bacnet_lights'),
    url(r'^v1/projectors/$', views_v1.ProjectorViewSet.as_view(), name='projectors'),
    url(r'^v1/crestons/$', views_v1.CrestonViewSet.as_view(), name='crestons'),

]
