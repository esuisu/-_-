from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанры книги",
                            verbose_name="Жанр книги")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите язык книги",
                            verbose_name="Язык книги")
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100,
                            help_text="Введите имя автора",
                            verbose_name="имя автора")

    last_name = models.CharField(max_length=100,
                                  help_text="Введите фамилию автора",
                                  verbose_name="фамилия автора")

    date_of_birth = models.DateField(
                                 help_text="Введите Дату рождения",
                                 verbose_name="Дата рождения")

    date_of_death = models.DateField(
        help_text="Введите Дату смерти",
        verbose_name="Дата смерти",
        null=True, blank=True)

    def __str__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200,
                            help_text="Введите название книги",
                            verbose_name="название книги")
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE,
                              help_text="Выберите жанр для книги",
                              verbose_name="жанр книги",null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text="Выберите язык для книги",
                                 verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author',
                             help_text="Введите автора книги",
                             verbose_name="автор книги")
    summary = models.TextField(max_length=1000,
                             help_text="Введите краткое описание книги",
                             verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13,
                             help_text="должно содержать 13 символов",
                             verbose_name="ISBN книги")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите статус экземпляра книги")
    def __str__(self):
        return self.name
class BookInstance(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=200, null=True,
                             help_text="Введите инвентарный номер книги",
                             verbose_name="инвентарный номер книги")
    imprint = models.CharField(max_length=200,
                             help_text="Введите издательство и год выпуска книги",
                             verbose_name="Издательство")
    status = models.ForeignKey('Status',on_delete=models.CASCADE,
                               null=True,
                               help_text="Введите состояник экземпляра",
                               verbose_name="статус экземпляра книги")

    due_back = models.DateField(null=True,blank=True,help_text="Введите конец срока статуса",
                                verbose_name="дата окончания статуса")
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 help_text="Выберите заказчика книги",
                                 verbose_name="Заказчик")

    @property
    def is_overdue(self):
       if self.due_back and date.today() > self.due_back:
          return True
       return False

    def __str__(self):
        return '%s %s %s' % (self.inv_nom , self.book, self.status)


class Course(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Введите название курса",
                            verbose_name=" название курса")
    lector = models.ManyToManyField('Lector',
                               help_text="выберите лектора",
                               verbose_name="лектора")
    description = models.TextField(max_length=200,
                            help_text="Введите описание",
                            verbose_name=" описание курса")
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=40,
                            help_text="Введите имя студента",
                            verbose_name="имя студента")

    def __str__(self):
        return self.name
class Lector(models.Model):
    name = models.CharField(max_length=40,
                            help_text="Введите имя лектора",
                            verbose_name="имя лектора")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=40,
                            help_text="Введите имя урока",
                            verbose_name="имя урока")
    curses = models.ManyToManyField('Course',
                                    help_text="выберите курсы студента",
                                    verbose_name="курсы студента")

    lector = models.ForeignKey('Lector',on_delete=models.CASCADE,
                               help_text="выберите лектора",
                               verbose_name="лектора")
    students = models.ManyToManyField('Student',
                             help_text="выберите студентов",)

    def __str__(self):
        return '%s %s ' % (self.name, self.lector)


