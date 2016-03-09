from django.shortcuts import render, render_to_response
from django.template import RequestContext


from siteprojects.models import Project, ProjectImage


def project_item(request, slug, template_name="siteprojects/project_item.html"):
	project = Project.objects.get(slug=slug)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))