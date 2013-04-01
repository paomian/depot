from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=100,unique=True)
	description=models.TextField()
	image_url=models.CharField(max_length=200)
	price=models.DecimalField(max_digits=8,decimal_places=2)
	date_available = models.DateField()
	def __unicode__(self):
		return self.title
class LineItem(models.Model):
	product = models.ForeignKey(Product)
	unit_price = models.DecimalField(max_digits=8,decimal_places=2)
	quantity = models.IntegerField()
