from django.forms import ModelForm, Select
from .models import Contacts

class ContactForm(ModelForm):
	class Meta:
		model = Contacts
		fields = '__all__'