from django.conf.urls import url
from cashpoint.views import *
#urls for cashpoint app

urlpatterns = [
    url(r'^productlist/$', ProductList.as_view()),
    url(r'^productdetails/(?P<pk>[0-9]+)/$', ProductDetails.as_view()),

]