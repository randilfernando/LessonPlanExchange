from django.utils.timezone import datetime

from django.db import models


class Subject(models.Model):
    subject = models.CharField(max_length=20, blank=False)


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False)
    topic = models.CharField(max_length=100, blank=False)


class Author(models.Model):
    email = models.CharField(max_length=100, blank=False, unique=True)
    password = models.TextField(blank=False)
    name = models.CharField(max_length=50, blank=False)


class LessonPLan(models.Model):
    medium = (
        ('SN', 'Sinhala'),
        ('TM', 'Tamil'),
        ('EN', 'English')
    )
    grade = (
        (6, 'Grade 06'),
        (7, 'Grade 07'),
        (8, 'Grade 08'),
        (9, 'Grade 09'),
        (10, 'Grade 10'),
        (11, 'Grade 11')
    )
    day = {
        (1, 'Day 1'),
        (2, 'Day 2'),
        (3, 'Day 3'),
        (4, 'Day 4'),
        (5, 'Day 5')
    }
    syllabus_year = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)
    link = models.TextField(blank=False)
    date_created = models.DateField(default=datetime.now)
    date_modified = models.DateField(default=datetime.now)


class Comment(models.Model):
    comment = models.TextField(blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)
    lesson_plan = models.ForeignKey(LessonPLan, on_delete=models.CASCADE, blank=False)
