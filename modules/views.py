from django.views.generic import ListView,TemplateView
import re
from modules.models import Module, Images, Spelling, \
RepeatSentence, AcademicVocabulary, Dictation, HighlightWords, \
SelectMissingWord, HighlightCorrectSummary, ReadTAloud, RetellLecture, Essay,\
FillInBlanks, AnswerShortQuestions, ReorderParagraph, MultipleSelection, MultipleSelectionReading,\
FillBlanksReading, SummarizeSpokenText,SummarizeWrittenText

class AbstractListView(ListView):
    
    def get_queryset(self):    
        qs = super().get_queryset() 
        queryset = qs.filter(active=True,free=True)
        return queryset
    class Meta:
        abstract = True

class ModuleListView(AbstractListView):
    model = Module
    template_name='modules\home.html'
    #paginate_by = 8
    

class ImagesListView(AbstractListView):
    model = Images
    template_name = 'questions\describe-image.html'
    paginate_by = 1

class SpellingListView(AbstractListView):
    model = Spelling
    template_name = 'questions\spelling.html'
    paginate_by = 10

class RepeatListView(AbstractListView):
    model = RepeatSentence
    template_name = 'questions\\repeat-sentence.html'
    paginate_by = 10

class AcademicVocabularyListView(AbstractListView):
    model = AcademicVocabulary
    template_name = 'questions\\academic-vocabulary.html'
    paginate_by = 10

class DictationListView(AbstractListView):
    model = Dictation
    template_name = 'questions\write-from-dictation.html'
    paginate_by = 2

class HighlightListView(AbstractListView):
    model = HighlightWords
    template_name = 'questions\highlight-incorrect-words.html'
    paginate_by = 1
    def get_queryset(self):
            queryset = super(HighlightListView,self).get_queryset()
            for item in queryset:
                paragraph = item.paragraph
                item.paragraph = paragraph.split()
                answers = item.answers
                item.answers = [ i.strip() for i in answers.split(',')]
                print(item.answers )
            return queryset
class SelectMissingWordView(AbstractListView):
    model = SelectMissingWord
    template_name = 'questions\select-missing-word.html'
    paginate_by = 1

class HighlightCorrectSummaryView(AbstractListView):
    model = HighlightCorrectSummary
    template_name = 'questions\highlight-correct-summary.html'
    paginate_by = 1

class ReadAloudView(AbstractListView):
    model = ReadTAloud
    template_name = 'questions\\read-aloud.html'
    paginate_by = 1

class RetellLectureView(AbstractListView):
    model = RetellLecture
    template_name = 'questions\\retell-lecture.html'
    paginate_by = 1

class EssayView(AbstractListView):
    model = Essay
    template_name = 'questions\write-essay.html'
    paginate_by = 1

class FillInBlanksView(AbstractListView):
    model = FillInBlanks
    template_name = 'questions\\fill-in-blanks.html'
    paginate_by = 1

    def get_queryset(self):
        queryset = super(FillInBlanksView, self).get_queryset()
        for item in queryset:
            answer_string = item.answers
            answer_list = answer_string.split(",")
            regex_words = re.compile('|'.join(map(re.escape,answer_list)))
            paragraph = regex_words.sub('XXXX',item.paragraph)
            item.paragraph = paragraph.split()
            item.answers = answer_list
            
        return queryset
class AnswerShortQuestionsView(AbstractListView):
    model = AnswerShortQuestions
    template_name = 'questions\spelling.html'
    paginate_by = 10

class ReorderParagraphView(AbstractListView):
    model = ReorderParagraph
    template_name = 'questions\\reorder-paragraph.html'
    paginate_by = 1
   
class MultipleSelectionView(AbstractListView):
    model = MultipleSelection
    template_name = 'questions\multiple-selection.html'
    paginate_by = 1

class MultipleSelectionReadingView(AbstractListView):
    model = MultipleSelectionReading
    template_name = 'questions\multiple-selection.html'
    paginate_by = 1

class FillBlanksReadingView(AbstractListView):
    model = FillBlanksReading
    template_name = 'questions\\fill-blanks-reading.html'
    paginate_by = 1
    def get_queryset(self):
        queryset = super(FillBlanksReadingView, self).get_queryset()
        for item in queryset:
            pr = (item.paragraph).split()
            item.answers = (item.answers).split(',')
            item.option_1 = (item.option_1).split(',')
            item.option_2 = (item.option_2).split(',')
            item.option_3 = (item.option_3).split(',')
            item.option_4 = (item.option_4).split(',')
            item.option_5 = (item.option_5).split(',')
            print(item.answers)
            print(pr)
            for i in pr:
                if i in item.answers:
                    pr[pr.index(i)]=i.upper()
            item.paragraph = pr  
        return queryset

class SummarizeSpokenTextView(AbstractListView):
    model = SummarizeSpokenText
    template_name = 'questions\summarize-spoken-text.html'
    paginate_by = 1

class SummarizeWrittenTextView(AbstractListView):
    model = SummarizeWrittenText
    template_name = 'questions\summarize-written-text.html'
    paginate_by = 1

# this is not working tke care of it later not urgent


class Template404View(TemplateView):
    template_name='modules\\404.html'