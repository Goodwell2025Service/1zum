from django.urls import path

from .views import about

app_name = 'company'

urlpatterns = [
	path('', about, name='about')
]
