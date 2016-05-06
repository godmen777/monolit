from django.contrib import admin
from django.db import models
from django.forms import Textarea
from core.models import Service, Post, Page, Review, Partner, Notes, Template
from image_cropping import ImageCroppingMixin
# from mptt_tree_editor.admin import TreeEditor
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


class ServiceAdmin(ImageCroppingMixin, DraggableMPTTAdmin):
		model = Service
		prepopulated_fields = {'slug': ('name',), }
		formfield_overrides = {
			models.TextField: {
				'widget': Textarea(attrs={
					'rows': 4,'cols': 40
				})
			},
		}
		list_display = ('tree_actions', 'indented_title', 'name', 'slug', 'published')
		list_display_links = ('indented_title', 'name',)

		def get_form(self, request, obj=None, **kwargs):
			form = super(ServiceAdmin, self).get_form(request, obj, **kwargs)
			form.base_fields['preview_text'].widget.attrs['style'] = 'width: 95%;'
			return form


class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
		model = Post
		prepopulated_fields = {'slug': ('name',), }
		formfield_overrides = {
			models.TextField: {
				'widget': Textarea(attrs={
					'rows': 4,'cols': 40
				})
			},
		}

		def get_form(self, request, obj=None, **kwargs):
			form = super(PostAdmin, self).get_form(request, obj, **kwargs)
			form.base_fields['preview_text'].widget.attrs['style'] = 'width: 95%;'
			return form


class PageAdmin(admin.ModelAdmin):
		model = Page
		prepopulated_fields = {'slug': ('name',), }

		class Media:
				js = ('admin/js/admin.js',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Review)
admin.site.register(Partner)
admin.site.register(Notes)
admin.site.register(Template)
