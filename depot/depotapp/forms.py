
from django import forms
from models import *
import itertools


def anyTure(predicate,sequence):
		return True in itertools.imap(predicate,sequence)
def endswith(s,*endings):
	return anyTure(s.endswith,endings)
class ProductForm(forms.ModelForm):
	
	class Meta:
		model = Product		
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		
	def clean_price(self):
		price=self.cleaned_data['price']
		if price <= 0:
			raise forms.ValidationError("price always >0")
		return price

	def clean_image_url(self):
		url=self.cleaned_data['image_url']
		if not endswith(url.lower(),'.jpg','.png','.gif'):
			raise forms.ValidationError("type error")
		return url
