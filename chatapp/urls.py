from django.conf.urls import patterns, include, url

urlpatterns =[
     url(r'/send','chatapp.views.send'),
     url(r'^', 'chatapp.views.index'),
]