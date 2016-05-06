#-*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from siteprojects.models import Project, Category, ProjectImage, Amenities, Garage
from image_cropping import ImageCroppingMixin
from ckeditor.widgets import CKEditorWidget


class ProjectImageInline(ImageCroppingMixin, admin.StackedInline):
    model = ProjectImage
    extra = 1


# class AmenitiesInline(admin.StackedInline):
#     model = Amenities
#     extra = 1


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    fieldsets = [
        (u'Параметры проекта', {'fields':['account','category','garage','name','slug','amenities']}),
        (u'Основная информация', {'fields':['combined_area','kubatura','building_area','square','ugol_inclination',
            'roof_area','dimensions_home']}),
        (u'Описание', {'fields': ['text']}),
        (u'Материал', {'fields': ['material']}),
    ]
    prepopulated_fields = {'slug': ('name', ), }
    filter_horizontal = ('amenities',)
    inlines = [ProjectImageInline, ]

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name', ), }

admin.site.register(Category, CategoryAdmin)    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Amenities)
admin.site.register(Garage)
