from django.shortcuts import render, render_to_response
from django.template import RequestContext
from configs.forms import ContactForm
from django.views.generic.edit import FormView
from siteprojects.models import Project
from core.models import Service, Post, Review, Partner, Page
from configs.methods import get_site_config


# def home(request, template_name="core/home.html"):
# 	form = ContactForm()
# 	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

class ContactFormView(FormView):
	template_name = "core/home.html"
	form_class = ContactForm
	success_url = "/success"

	def get_context_data(self, **kwargs):
		context = super(ContactFormView, self).get_context_data(**kwargs)
		context['project_list'] = Project.objects.all()
		context['service_list'] = service_list = Service.objects.all()
		context['service_main'] = service_list.get(is_main=True)
		context['post_list'] = Post.objects.all()
		context['review_list'] = Review.objects.all()
		context['partner_list'] = Partner.objects.all()
		context['page_list'] = Page.objects.all()
		context['config'] = get_site_config(self.request)
		return context

	def form_valid(self, form):
		form.send_email(self.request)
		return super(ContactFormView, self).form_valid(form)


def success(request, template_name="configs/success.html"):
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))