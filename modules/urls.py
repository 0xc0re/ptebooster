from django.urls import path, re_path
from modules.views import ModuleListView,ImagesListView,SpellingListView, \
Template404View, RepeatListView, AcademicVocabularyListView, DictationListView, \
HighlightListView, SelectMissingWordView, HighlightCorrectSummaryView, ReadAloudView, \
RetellLectureView, EssayView, FillInBlanksView, AnswerShortQuestionsView, ReorderParagraphView, \
MultipleSelectionView, MultipleSelectionReadingView, FillBlanksReadingView, SummarizeSpokenTextView

urlpatterns = [
    path('', ModuleListView.as_view()),
    path('describe-image/', ImagesListView.as_view()),
    path('spelling/', SpellingListView.as_view()),
    path('repeat-sentence/', RepeatListView.as_view()),
    path('academic-vocabulary-builder/', AcademicVocabularyListView.as_view()),
    path('write-from-dictation/', DictationListView.as_view()),
    path('highlight-incorrect-words/', HighlightListView.as_view()),
    path('highlight-correct-summary/', HighlightCorrectSummaryView.as_view()),
    path('select-missing-word/', SelectMissingWordView.as_view()),
    path('read-aloud/', ReadAloudView.as_view()),
    path('retell-lecture/', RetellLectureView.as_view()),
    path('write-essay/',EssayView.as_view()),
    path('fill-in-blanks/',FillInBlanksView.as_view()),
    path('answer-short-question/',AnswerShortQuestionsView.as_view()),
    path('reorder-paragraphs/',ReorderParagraphView.as_view()),
    path('multiple-selection-listening/',MultipleSelectionView.as_view()),
    path('multiple-selection-reading/',MultipleSelectionReadingView.as_view()),
    path('fill-blanks-reading/',FillBlanksReadingView.as_view()),
    path('summarize-spoken-text/',SummarizeSpokenTextView.as_view()),
    re_path('^$',Template404View.as_view()),
]