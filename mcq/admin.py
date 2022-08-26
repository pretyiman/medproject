# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from mcq.models import Answers,Subject,Topic,Question,Quiz,PublicMcq,PublicAnswers
# from bookstore.models import Catagory,Writter,Book
# from blog.models import Post,Comment
# from userdata.models import Profile
# Register your models here.


admin.site.register(Quiz)
admin.site.register(Topic)
# admin.site.register(Catagory)
# admin.site.register(Writter)
# admin.site.register(Book)
# admin.site.register(OneLiner)
admin.site.register(PublicMcq)

# blog
# admin.site.register(Post)
# admin.site.register(Comment)

class TopicInLine(admin.TabularInline):
    model = Topic
    extra =0

class SubjectAdmin(admin.ModelAdmin):
    inlines = [TopicInLine,]


class AnswerInline(admin.TabularInline):
    model = Answers
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    list_display = ('subject', 'topic', 'desciption')


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'date_of_birth','photo')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Subject, SubjectAdmin)
# admin.site.register(Profile,ProfileAdmin)

class PublicAnswersInline(admin.TabularInline):
    model = PublicAnswers
    extra = 4


class PublicMcqAdmin(admin.ModelAdmin):
    inlines = [PublicAnswersInline, ]
    list_display = ('subject', 'topic', 'question')


# admin.site.register(PublicMcq, PublicMcqAdmin)
# admin.site.register(PublicAnswers, PublicAnswersAdmin)
