from django import forms
from .models import *


class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('name','email')