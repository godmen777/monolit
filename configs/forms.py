# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail
from methods import get_site_config
from siteprojects.models import Project


class ProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Ваше имя', 'class': 'form-control'}
        self.fields['phone'].widget.attrs = {'placeholder': 'Ваш телефон', 'class': 'form-control'}
        self.fields['name'].label = ""
        self.fields['phone'].label = ""
        name = forms.CharField()
        phone = forms.CharField()
        project = forms.IntegerField(widget=forms.HiddenInput)

        class Meta:
            fields = [
                'name',
                'phone',
                'project',
            ]
            labels = {
                "name": u"",
                "phone": u""
            }

            def send_email(self, request):
                data = self.cleaned_data
                # получаем данные конфигурации сайта
                config = get_site_config(request)
                project = Project.objects.get(id=data['project'])
                # отправка формы
                subject = u'Контактные данные пользователя %s' % config.site.domain
                message = u'Имя: %s \n телефон: %s \n Название проекта: %s' % (data['name'], data['phone'], project.name)
                send_mail(subject, message, 'teamer777@gmail.com', [config.site_email], fail_silently=False)


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Ваше имя', 'class': 'contact-form black'}
        self.fields['phone'].widget.attrs = {'placeholder': 'Ваш телефон', 'class': 'contact-form black'}
        self.fields['name'].label = ""
        self.fields['phone'].label = ""
        name = forms.CharField()
        phone = forms.CharField()

        class Meta:
            fields = [
                'name',
                'phone'
            ]
            labels = {
                "name": u"",
                "phone": u""
            }

            def send_email(self, request):
                data = self.cleaned_data
                # получаем данные конфигурации сайта
                config = get_site_config(request)
                # отправка формы
                subject = u'Контактные данные пользователя %s' % config.site.domain
                message = u'Имя: %s \n телефон: %s' % (data['name'], data['phone'])
                send_mail(subject, message, 'teamer777@gmail.com', [config.site_email], fail_silently=False)


class SubscribeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Ваше имя', 'class': 'contact-form'}
        self.fields['email'].widget.attrs = {'placeholder': 'Ваш email', 'class': 'contact-form'}
        self.fields['phone'].widget.attrs = {'placeholder': 'Ваш телефон', 'class': 'contact-form'}
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['phone'].label = ""
        name = forms.CharField()
        phone = forms.CharField()
        email = forms.EmailField()

        class Meta:
            fields = [
                'name',
                'phone',
                'email',
            ]
            labels = {
                "name": u"",
                "phone": u"",
                "email": u"",
            }

            def send_email(self, request):
                data = self.cleaned_data
                # получаем данные конфигурации сайта
                config = get_site_config(request)
                # отправка формы
                subject = u'Подписка пользователя %s' % config.site.domain
                message = u'Имя: %s \n телефон: %s \n email: %s' % (data['name'], data['phone'], data['email'])
                send_mail(subject, message, 'teamer777@gmail.com', [config.site_email], fail_silently=False)
