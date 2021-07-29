from django.contrib import admin

# Register your models here.
from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    fields = ["pub_date", "question_text"]
    list_filter = ["pub_date"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)