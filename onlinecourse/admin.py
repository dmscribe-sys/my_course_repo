from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Inline for Choices inside Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# Admin for Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Admin for Lesson
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Admin for Question with inline Choices
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

# Register models in admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
