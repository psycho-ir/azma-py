from django.db import models


class ExamCategory(models.Model):
    name = models.CharField(max_length=200)

    def number_of_exams(self):
        return self.exam_set.count()


class Exam(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    category = models.ForeignKey(ExamCategory)


    def __str__(self):
        return str(self.pk) + " " + self.name


class Question(models.Model):
    text = models.CharField(max_length=500)
    exam = models.ForeignKey(Exam)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question)

    def __str__(self):
        return str(self.pk) + " " + self.text


class MultipleChoice(Choice):
    valid = models.BooleanField()


