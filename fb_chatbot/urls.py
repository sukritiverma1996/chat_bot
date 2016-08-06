from django.conf.urls import patterns, url
from fb_chatbot import views
from fb_chatbot.views import MyQuoteBotView

# r'^$' is a regex string
# It deals with empty URLs
urlpatterns = patterns('',
    url(r'^$', views.hello_world, name = 'hello_world'),
    url(r'^hi/$', views.hello, name = 'hello'),
    url(r'^hi/hello$', views.hello, name = 'hello'),
    url(r'^facebook_auth/$', MyQuoteBotView.as_view()),)