from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Group, Lesson, Grade, Student

class GroupListView(ListView):
    model = Group
    template_name = "education/group_list.html"

class GroupDetailView(DetailView):
    model = Group
    template_name = "education/group_detail.html"

class ScheduleView(ListView):
    model = Lesson
    template_name = "education/schedule.html"

    def get_queryset(self):
        return Lesson.objects.filter(
            group_id=self.kwargs["group_id"]
        ).order_by("day", "lesson_number")

class StudentGradesView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "education/grades.html"

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        return Grade.objects.filter(student=student)

class GradeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Grade
    fields = ("student", "lesson", "value")
    template_name = "education/grade_form.html"

    def test_func(self):
        return hasattr(self.request.user, "teacher")

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        return super().form_valid(form)