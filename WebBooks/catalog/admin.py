from django.contrib import admin

# Register your models here.
from .models import Genre,Language,Author,Book,Status,BookInstance,Course,Student,Lector,Group
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Status)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lector)
admin.site.register(Group)
@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
   list_filter = ('book', 'status')
   list_display = ('book', 'status','borrower', 'due_back', 'id')
   fieldsets = [
      ('Book',{'fields': ('book', 'imprint','inv_nom')}),
      ('Status', {'fields': ('status', 'due_back', 'borrower')}),
      ]