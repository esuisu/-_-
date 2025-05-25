from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Genre,Language,Author,Book,Status,BookInstance,Course,Student,Lector,Group
from .forms import AuthorsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Create your views here.
class BookListView(generic.ListView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class BookDetailView(generic.DetailView):
    model = Book

def index(request):
    num_books = Book.objects.all().count()
    num_instances =BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'index.html',
                  context={'num_books':num_books,
                           'num_instances':num_instances,
                           'num_instances_available':num_instances_available,
                           'num_authors ':num_authors,
                           'num_visits':num_visits,
                  },)

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
   model = BookInstance
   template_name = 'catalog/bookinstance_list_borrowed_user.html'
   paginate_by = 10
   def get_queryset(self):
      return BookInstance.objects.filter(
      borrower=self.request.user).filter(
      status__exact='2').order_by('due_back')

def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm
    return render(request , 'catalog/author_add.html',
                  {"form":authorsform, "author":author})
def create(request):
   if request.method == "POST":
      author = Author()
      author.first_name = request.POST.get("first_name")
      author.last_name = request.POST.get("last_name")
      author.data_of_birth = request.POST.get("date_of_birth")
      author.data_of_death = request.POST.get("date_of_death")
      author.save()
      return HttpResponseRedirect("/authors_add/")

def delete(request, id):
   try:
      author = Author.objects.get(id=id)
      author.delete()
      return HttpResponseRedirect("/authors_add")
   except Author. DoesNotExist:
      return HttpResponseNotFound("<h2>Author not found</h2>")

def edit1(request, id):
   author = Author.objects.get(id=id)
   if request.method == "POST":
      author.first_name = request.POST.get("first_name")
      author.last_name = request.POST.get("last_name")
      author.data_of_birth = request.POST.get("date_of_birth")
      author.data_of_death = request.POST.get("date_of_death")
      author.save()
      return HttpResponseRedirect("/author_add/")
   else:
      return render (request,"catalog/edit1.html",{"author": author})

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookDelete(UpdateView):
    model = Book
    success_url = reverse_lazy('books')