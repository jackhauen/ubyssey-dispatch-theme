from django.conf.urls import patterns, include, url
from views import UbysseyTheme

theme = UbysseyTheme()

theme_urls = patterns('',
    url(r'^$', theme.home, name='home'),
    url(r'^search/$', theme.search, name='search'),
    url(r'^author/(?P<slug>[-\w]+)/articles/$', theme.author_articles, name='author-articles'),
    url(r'^author/(?P<slug>[-\w]+)/$', theme.author, name='author'),
    url(r'^topic/(\d*)/$', theme.topic, name='topic'),
    url(r'^(?P<section>[-\w]+)/(?P<slug>[-\w]+)/$', theme.article, name='article'),
    url(r'^(?P<slug>[-\w]+)/$', theme.section, name='page'),
)
