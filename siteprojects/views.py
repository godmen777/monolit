from django.shortcuts import render, render_to_response
from django.template import RequestContext
from configs.forms import ProjectForm


from siteprojects.models import Project, ProjectImage
from core.models import Post


def project_item(request, slug, template_name="siteprojects/project_item.html"):
	project = Project.objects.get(slug=slug)
	performer_profile = project.account.performer_of_account
	featured_projects = Project.objects.filter(featured=True)
	form = ProjectForm(initial={'project':project.id,})
	if request.POST:
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.send_email(request)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def project_list(request, template_name="siteprojects/project_list.html"):
	posts = Post.objects.all()[:5]
	area_min = request.GET.get('area_min','')
	area_max = request.GET.get('area_max','')
	category_id = request.GET.get('category_id','')
	if area_min and area_max:
		projects = Project.objects.filter(combined_area__gte=int(area_min)).filter(combined_area__lte=int(area_max))
	elif category_id:
		projects = Project.objects.filter(category_id__exact=int(category_id))
	else: 
		projects = Project.objects.all()	

		
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))