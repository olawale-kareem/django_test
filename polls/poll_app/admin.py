from django.contrib import admin
from .models import Question, Choice

# basic admin interface
# admin.site.register(Question)


# customised admin interface
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)


# customised admin interface: separated fields

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
admin.site.register(Question, QuestionAdmin)

# adding related objects
# adding Choice model
admin.site.register(Choice)