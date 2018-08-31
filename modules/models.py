from django.db import models

class Module(models.Model):
    module_name = models.CharField(max_length=80)
    question_class = models.CharField(max_length=80, blank=True)
    module_image=models.ImageField(upload_to='ptebooster/media/images',default='ptebooster/media/images/module_default.png')
    slug = models.SlugField(max_length=80, unique=True)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return self.module_name


class Images(models.Model):
    image_question=models.ImageField(upload_to='ptebooster/media/images',verbose_name='Image')

    class Meta:
        ordering = ['-id']

class Spelling(models.Model):
    word = models.CharField(max_length=100, blank=False)
    audio = models.FileField(upload_to='ptebooster/media/spelling-audio')

"""SENTENCE_CHOICES=[
    ('L','Listening'),
    ('S','Speaking'),
]"""
class RepeatSentence(models.Model):
    sentence_example = models.CharField(max_length=300, blank=False)
    audio = models.FileField(upload_to='ptebooster/media/sentences')
    #main_section = models.CharField(max_length=100, choices=SENTENCE_CHOICES, default='S')

class Dictation(models.Model):
    sentence_example = models.CharField(max_length=300, blank=False)
    audio = models.FileField(upload_to='ptebooster/media/dictation')

class AcademicVocabulary(models.Model):
    word = models.CharField(max_length=150, blank=False)
    academic_in_sentence = models.CharField(max_length=300, blank=False)

class HighlightWords(models.Model):
    paragraph = models.TextField(max_length=800,blank=False)
    audio = models.FileField(upload_to='ptebooster/media/highlight-incorrect-words')
    answers = models.CharField(max_length=300, blank=False)
    correct_words = models.CharField(max_length=300, blank=True)

class AbstractChoices(models.Model):
    option_1 = models.TextField(max_length=500, blank=False)
    option_2 = models.TextField(max_length=500, blank=False)
    option_3 = models.TextField(max_length=500, blank=False)
    option_4 = models.TextField(max_length=500, blank=False)
    answer = models.TextField(max_length=500, blank=False)

    class Meta:
        abstract = True

class SelectMissingWord(AbstractChoices):
    audio_topic = models.CharField(max_length=100, blank=False)
    audio = models.FileField(upload_to='ptebooster/media/select-missing-word')
    

class HighlightCorrectSummary(AbstractChoices):
    paragraph = models.TextField(max_length=1000,blank=False)
    audio = models.FileField(upload_to='ptebooster/media/highlight-correct-summary')
    

class  ReadTAloud(models.Model):
    paragraph = models.TextField(max_length=1000,blank=False)
    audio = models.FileField(upload_to='ptebooster/media/read-aloud',blank=True)
    
class RetellLecture(models.Model):
    lecture = models.TextField(max_length=1000,blank=True)
    audio = models.FileField(upload_to='ptebooster/media/retell-lecture',blank=True)
    video = models.FileField(upload_to='ptebooster/media/retell-lecture',blank=True)
    image = models.FileField(upload_to='ptebooster/media/retell-lecture',blank=True)

class Essay(models.Model):
    topic = models.TextField(max_length=1000,blank=False)
    
class FillInBlanks(models.Model):
    paragraph = models.TextField(max_length=1000,blank=False)
    audio = models.FileField(upload_to='ptebooster/media/fill-in-blanks',blank=False)
    answers = models.CharField(max_length=300,blank=False)

class AnswerShortQuestions(models.Model):
    audio = models.FileField(upload_to='ptebooster/media/answer-short-question',blank=False)
    answer = models.CharField(max_length=90,blank=False)

class ReorderParagraph(AbstractChoices):
    option_5 = models.CharField(max_length=150,blank=False)
    

class AbstractSelection(models.Model):
    paragraph = models.TextField(max_length=600,blank=True)
    option_1 = models.CharField(max_length=150,blank=False)
    option_2 = models.CharField(max_length=150,blank=False)
    option_3 = models.CharField(max_length=150,blank=False)
    option_4 = models.CharField(max_length=150,blank=False)
    option_5 = models.CharField(max_length=150,blank=True)
    option_6 = models.CharField(max_length=150,blank=True)
    answers = models.CharField(max_length=150,blank=False)

    class Meta:
        abstract = True

class MultipleSelection(AbstractSelection):
    audio = models.FileField(upload_to='ptebooster/media/multiple-selection-listening',blank=False)
    

class MultipleSelectionReading(AbstractSelection):
    paragraph = models.TextField(max_length=1000,blank=False)
    

class FillBlanksReading(AbstractSelection):
    paragraph = models.TextField(max_length=1000,blank=False)

class SummarizeSpokenText(models.Model):
    paragraph = models.TextField(max_length=1000,blank=False)
    audio = models.FileField(upload_to='ptebooster/media/summarize-spoken-text',blank=False)
    model_answer = models.TextField(max_length=1000,blank=True)


class SummarizeWrittenText(models.Model):
    paragraph = models.TextField(max_length=1000,blank=False)
    model_answer = models.TextField(max_length=1000,blank=True)