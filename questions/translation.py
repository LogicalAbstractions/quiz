from modeltranslation.translator import translator, TranslationOptions

from questions.models import Question, Answer, Tag


class TagTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('en', 'de')


class QuestionTranslationOptions(TranslationOptions):
    fields = ('text', 'explanation')
    required_languages = {
        'de': ('text',)
    }


class AnswerTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('de',)


translator.register(Tag, TagTranslationOptions)
translator.register(Question, QuestionTranslationOptions)
translator.register(Answer, AnswerTranslationOptions)
