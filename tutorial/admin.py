from django.contrib import admin
from django import forms
from tutorial.models import *
from tutorial.forms.TutorialForm import TutorialForm


class ChoiceForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)


class QuestionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    code = forms.CharField(widget=forms.Textarea, required=False)


class ChoiceInline(admin.TabularInline):
    model = TutorialChoice
    extra = 4
    form = ChoiceForm


class QuestionInline(admin.TabularInline):
    model = TutorialQuestion
    readonly_fields = ['exam']
    extra = 0


class QueAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class ChoAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    form = ChoiceForm


class TutorialAdmin(admin.ModelAdmin):
    form = TutorialForm


admin.site.register(TutorialCategory)
admin.site.register(TutorialQuestion, ChoAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialExam, QueAdmin)
