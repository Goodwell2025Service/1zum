from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView

from .models import AboutUs


class AboutDetail(DetailView):
	model = AboutUs

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		return ctx


about_view = AboutDetail.as_view()