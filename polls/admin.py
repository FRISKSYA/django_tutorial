from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		("Main question", {"fields": ["question_text"]}),
		("Data information", {"fields": ["pub_date"], "classes": ["collapse"]}),
	]
	inlines = [ChoiceInline]
	list_display = ["question_text", "pub_date", "was_published_recently"]
	list_filter = ["pub_date"]
	search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
