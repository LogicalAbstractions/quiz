from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import InlineModelAdmin, TabularInline
from django.http import HttpResponseRedirect

from questions.models import Question, Answer, Tag, Fact


class AnswerAdmin(TabularInline):
    model = Answer
    exclude = ('text',)
    extra = 0


class TagAdmin(ModelAdmin):
    exclude = ('text',)


class FactAdmin(ModelAdmin):
    list_display = ('slug', 'tag_text')
    exclude = ('slug',)


class QuestionAdmin(ModelAdmin):
    list_display = ('slug', 'tag_text', 'created_by', 'verified_by', 'is_active')
    inlines = [AnswerAdmin]
    readonly_fields = ('created_by', 'verified_by')
    exclude = ('text', 'explanation','slug')

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['can_verify'] = False
        extra_context['can_unverify'] = False

        if object_id:
            question = Question.objects.get(pk=object_id)
            extra_context['can_verify'] = question.can_verify(request)
            extra_context['can_unverify'] = question.verified_by is not None

        return super(QuestionAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def response_change(self, request, obj: Question):
        if "_verify" in request.POST:

            if obj.can_verify(request):
                obj.verify(request)
                self.message_user(request, "This question has been verified")
            else:
                self.message_user(request, "Cannot verify question")

            return HttpResponseRedirect(".")

        if "_unverify" in request.POST:
            if obj.verified_by:
                obj.verified_by = None
                obj.save()

            return HttpResponseRedirect(".")

        return super().response_change(request, obj)

    def save_model(self, request, obj: Question, form, change):

        if not change:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Fact, FactAdmin)

admin.site.site_header = 'Quiz questions'
