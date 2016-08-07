
# r'^$' is a regex string
# It deals with empty URLs
from django.conf.urls import patterns,url
from fb_chatbot import views
from .views import MyQuoteBotView


urlpatterns = patterns('', 
    url(r'^$', views.index,name = 'index'), 
    url(r'^facebook_auth/?$', MyQuoteBotView.as_view()))
