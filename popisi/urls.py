
from django.conf.urls import url
from popisi.views import ZvrstListView, PostavkaFilter
#from popisi.views import PostavkaListView,
#from popisi.views import VrstaDelListView,
#from popisi.views import SkupinaListView,

from popisi.views import PostavkaDetailView,VrstaDelDetailView,SkupinaDetailView,ZvrstDetailView,DelPostavkeDetailView
from . import views


urlpatterns = [
    
    url(r'^$', views.index, name='index'),
        
    #url(r'^postavke/$', views.PostavkaListView.as_view(), name='postavke'),
    url(r'^postavka_detail/(?P<pk>\d+)/$',views.PostavkaDetailView.as_view(), name='postavka-detail'),
    url(r'^postavka_filter/$', views.PostavkaFilter.as_view(), name='filter'),
    

    url(r'^del_postavke_detail/(?P<pk>\d+)/$',views.DelPostavkeDetailView.as_view(), name='del_postavke-detail'),


    #url(r'^vrsta_del/$', views.VrstaDelListView.as_view(), name='vrsta_del'),
    url(r'^vrsta_del_detail(?P<pk>\d+)$',views.VrstaDelDetailView.as_view(), name='vrsta_del-detail'),

    #url(r'^skupina/$', views.SkupinaListView.as_view(), name='skupina'),
    url(r'^skupina_detail(?P<pk>\d+)$',views.SkupinaDetailView.as_view(), name='skupina-detail'),

    url(r'^zvrst/$', views.ZvrstListView.as_view(), name='zvrst'),
    url(r'^zvrst_detail(?P<pk>\d+)$',views.ZvrstDetailView.as_view(), name='zvrst-detail'),

]

urlpatterns += [  
    url(r'^skupina/nova/$', views.SkupinaCreate.as_view(), name='skupina_nova'),
    url(r'^skupina/(?P<pk>\d+)/popravi/$', views.SkupinaUpdate.as_view(), name='skupina_popravi'),
    url(r'^skupina/(?P<pk>\d+)/odstrani/$', views.SkupinaDelete.as_view(), name='skupina_odstrani'),
]



#vaje lahko zbrises

urlpatterns += [  
    url(r'^a/$', views.get_ime, name='tvoje-ime'),
    url(r'^skupina/$', views.get_skupina, name='skupina'),
]