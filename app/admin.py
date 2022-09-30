from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display=['name',]

@admin.register(models.quizes)
class QuizAdmin(admin.ModelAdmin):
    list_display=['id','title',]


class AnswerInlineModel(admin.TabularInline):
    model=models.answers
    list_display=['answer_text','is_right']

@admin.register(models.questions)
class QuestionAdmin(admin.ModelAdmin):
    fields=['title','quiz',]
    list_display=['title','quiz','date_created']
    inlines=[AnswerInlineModel,]

@admin.register(models.answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display=['answer_text','is_right','question']