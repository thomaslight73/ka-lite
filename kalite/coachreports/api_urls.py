from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('coachreports.api_views',
    url(r'data/$',  'api_data', {}, 'api_data'),
)

