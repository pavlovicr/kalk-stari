
from django.conf.urls import url
from popisi.views import PostavkaListView,P,PostavkaFilter
from popisi.views import PostavkaDetailView 

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^[0-9]+/$', views.vaja, name='vaja'),
    url(r'^postavke/$', views.PostavkaListView.as_view(), name='postavke'),
    url(r'^filter/$', views.PostavkaFilter.as_view(), name='filter'),
    url(r'^p/$', views.P.as_view(), name='p'),
    url(r'^postavke/(?P<pk>\d+)/$',views.PostavkaDetailView.as_view(), name='postavka-detail'),
]