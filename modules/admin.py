from django.contrib import admin
from .models import Module, Images, Spelling, \
RepeatSentence, AcademicVocabulary, Dictation, HighlightWords,FillInBlanks, \
SelectMissingWord, HighlightCorrectSummary, ReadTAloud, RetellLecture, Essay, \
AnswerShortQuestions, ReorderParagraph, MultipleSelection, MultipleSelectionReading, \
FillBlanksReading, SummarizeSpokenText, SummarizeWrittenText

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['module_name', 'slug', 'description','question_class']
    prepopulated_fields = {'slug':('module_name',)}

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image_question']


@admin.register(Spelling)
class SpellingAdmin(admin.ModelAdmin):
    list_display = ['word','audio']

@admin.register(RepeatSentence)
class RepeatSentenceAdmin(admin.ModelAdmin):
    list_display = ['sentence_example','audio'] #,'main_section'

@admin.register(Dictation)
class DictationAdmin(admin.ModelAdmin):
    list_display = ['sentence_example','audio'] #,'main_section'

@admin.register(AcademicVocabulary)
class AcademicVocabularyAdmin(admin.ModelAdmin):
    list_display = ['word','academic_in_sentence']

@admin.register(HighlightWords)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','answers']

@admin.register(SelectMissingWord)
class SelectMissingWordAdmin(admin.ModelAdmin):
    list_display = ['audio_topic','audio','option_1', 'option_2','option_3','option_4','answer']

@admin.register(HighlightCorrectSummary)
class HighlightCorrectSummaryAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','option_1', 'option_2','option_3','option_4','answer']

@admin.register(ReadTAloud)
class ReadAloudAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio']

@admin.register(RetellLecture)
class RetellLectureAdmin(admin.ModelAdmin):
    list_display = ['lecture','audio','video','image']
    
@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    list_display = ['topic']

@admin.register(FillInBlanks)
class FillinBlanksAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','answers']

@admin.register(AnswerShortQuestions)
class FillinBlanksAdmin(admin.ModelAdmin):
    list_display = ['audio','answer']

@admin.register(ReorderParagraph)
class ReorderParagraphAdmin(admin.ModelAdmin):
    list_display = ['option_1','option_2','option_3','option_4','option_5','answer']

@admin.register(MultipleSelection)
class MultipleSelectionAdmin(admin.ModelAdmin):
    list_display = ['audio','option_1','option_2','option_3','option_4','option_5','option_6','answers']

@admin.register(MultipleSelectionReading)
class MultipleSelectionReadingAdmin(admin.ModelAdmin):
    list_display = ['paragraph','option_1','option_2','option_3','option_4','option_5','option_6','answers']

@admin.register(FillBlanksReading)
class FillBlanksReadingAdmin(admin.ModelAdmin):
    list_display = ['paragraph','option_1','option_2','option_3','option_4','option_5','option_6','answers']

@admin.register(SummarizeWrittenText)
class SummarizeWrittenTextAdmin(admin.ModelAdmin):
    list_display = ['paragraph','model_answer']
