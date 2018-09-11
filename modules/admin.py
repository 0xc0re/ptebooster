from django.contrib import admin
from .models import Module, Images, Spelling, \
RepeatSentence, AcademicVocabulary, Dictation, HighlightWords,FillInBlanks, \
SelectMissingWord, HighlightCorrectSummary, ReadTAloud, RetellLecture, Essay, \
AnswerShortQuestions, ReorderParagraph, MultipleSelection, MultipleSelectionReading, \
FillBlanksReading, SummarizeSpokenText, SummarizeWrittenText

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['module_name', 'slug', 'description','question_class','active']
    prepopulated_fields = {'slug':('module_name',)}

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id','image_question','active']


@admin.register(Spelling)
class SpellingAdmin(admin.ModelAdmin):
    list_display = ['item','audio','active']

@admin.register(RepeatSentence)
class RepeatSentenceAdmin(admin.ModelAdmin):
    list_display = ['item','audio','active'] #,'main_section'

@admin.register(Dictation)
class DictationAdmin(admin.ModelAdmin):
    list_display = ['item','audio','active'] #,'main_section'

@admin.register(AcademicVocabulary)
class AcademicVocabularyAdmin(admin.ModelAdmin):
    list_display = ['word','academic_in_sentence','active']

@admin.register(HighlightWords)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','answers','active']

@admin.register(SelectMissingWord)
class SelectMissingWordAdmin(admin.ModelAdmin):
    list_display = ['audio_topic','audio','option_1', 'option_2','option_3','option_4','answer','active']

@admin.register(HighlightCorrectSummary)
class HighlightCorrectSummaryAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','option_1', 'option_2','option_3','option_4','answer','active']

@admin.register(ReadTAloud)
class ReadAloudAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','active']

@admin.register(RetellLecture)
class RetellLectureAdmin(admin.ModelAdmin):
    list_display = ['lecture','audio','video','image','active']
    
@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    list_display = ['topic','active']

@admin.register(FillInBlanks)
class FillinBlanksAdmin(admin.ModelAdmin):
    list_display = ['paragraph','audio','answers','active']

@admin.register(AnswerShortQuestions)
class AnswerShortQuestions(admin.ModelAdmin):
    list_display = ['audio','item','active']

@admin.register(ReorderParagraph)
class ReorderParagraphAdmin(admin.ModelAdmin):
    list_display = ['option_1','option_2','option_3','option_4','option_5','answer','active']

@admin.register(MultipleSelection)
class MultipleSelectionAdmin(admin.ModelAdmin):
    list_display = ['audio','option_1','option_2','option_3','option_4','option_5','option_6','answers','active']

@admin.register(MultipleSelectionReading)
class MultipleSelectionReadingAdmin(admin.ModelAdmin):
    list_display = ['paragraph','option_1','option_2','option_3','option_4','option_5','option_6','answers','active']

@admin.register(FillBlanksReading)
class FillBlanksReadingAdmin(admin.ModelAdmin):
    list_display = ['paragraph','option_1','option_2','option_3','option_4','option_5','option_6','answers','active']

@admin.register(SummarizeWrittenText)
class SummarizeWrittenTextAdmin(admin.ModelAdmin):
    list_display = ['paragraph','model_answer','active']
