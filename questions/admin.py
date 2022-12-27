from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import InlineModelAdmin, TabularInline

from questions.models import Question, Answer, Tag


class AnswerAdmin(TabularInline):
    model = Answer
    exclude = ('text',)
    extra = 0


class TagAdmin(ModelAdmin):
    exclude = ('text',)


class QuestionAdmin(ModelAdmin):
    list_display = ('slug', 'tag_text', 'created_by', 'verified_by')
    inlines = [AnswerAdmin]
    readonly_fields = ('created_by', 'slug', 'verified_by')
    exclude = ('text',)

    def save_model(self, request, obj: Question, form, change):
        if not change:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.site_header = 'Quiz questions'
