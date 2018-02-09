from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class QuestionAdmin2(admin.ModelAdmin):
    fields = ['question_text', 'pub_date']
admin.site.register(Question, QuestionAdmin2)
