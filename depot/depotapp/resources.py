from django.core.urlresolvers import reverse
from rest_framework.views import View
from rest_framework.resources import ModelResource
from models import *


class LineItemResource(ModelResource):
	model = LineItem
	fields = ('product','unit_price','quantity')
	def product(self,instance):
		return instance.product.title
