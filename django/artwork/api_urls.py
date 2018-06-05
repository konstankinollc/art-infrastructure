from django.conf.urls import url

from artwork.api.v1 import views as views_v1

urlpatterns = [
    url(r'^v1/artists/$', views_v1.ArtistViewSet.as_view(), name='artists'),
    url(r'^v1/artists/(?P<paginate>\w+)/$', views_v1.ArtistViewSet.as_view(), name='artists'),
    url(r'^v1/artist_groups/$', views_v1.ArtistGroupViewSet.as_view(), name='artist_groups'),
    url(r'^v1/artist_groups/(?P<paginate>\w+)/$', views_v1.ArtistGroupViewSet.as_view(), name='artist_groups'),
    url(r'^v1/photos/$', views_v1.PhotoViewSet.as_view(), name='photos'),
    url(r'^v1/photos/(?P<paginate>\w+)/$', views_v1.PhotoViewSet.as_view(), name='photos'),
    url(r'^v1/documents/$', views_v1.DocumentViewSet.as_view(), name='documents'),
    url(r'^v1/equipment_types/$', views_v1.EquipmentTypeViewSet.as_view(), name='equipment_types'),
    url(r'^v1/equipment_types/(?P<paginate>\w+)/$', views_v1.EquipmentTypeViewSet.as_view(), name='equipment_types'),
    url(r'^v1/equipments/$', views_v1.EquipmentViewSet.as_view(), name='equipments'),
    url(r'^v1/installation_sites/$', views_v1.InstallationSiteViewSet.as_view(), name='installation_sites'),
    url(r'^v1/installations/$', views_v1.InstallationViewSet.as_view(), name='installations'),
    url(r'^v1/system_status/$', views_v1.SystemStatusViewSet.as_view(), name='system_status'),
]
