
from django.conf.urls.defaults import *
from models import *
from views import *
from rest_framework.views import APIView
from resource import *

urlpatterns = patterns('',

    (r'product/create/$', create_product),
    (r'product/list/$', list_product ),
    (r'product/edit/(?P<id>[^/]+)/$', edit_product),
    (r'product/view/(?P<id>[^/]+)/$', view_product),
    (r'^store/', store_view),
    (r'^cart/view/', view_cart),
	(r'cart/add/(?P<id>[^/]+)/$',add_to_cart),
	(r'cart/clean',clean_cart),
#	(r'API/cart/items',APIView.as_view(resource=LineItemResource)),
	)
