from django.conf.urls import url
from front import views


#urlpatterns = [
    #url(r'^$', views.index, name = 'index'),
    #url(r'^/detail/$', views.detail, name = 'detail')
#]


urlpatterns = [
    url(r'^(?P<institution_id>\d+)/detail/$', views.detail, name='detail'),
    url(r'^(\D+)/(\D+)/(\D+)/results/$', views.results, name='results'),
    url(r'^$', views.index, name='index'),

    #url(r'^/detail/$', views.detail, name='detail')
    # ... your url patterns
]
