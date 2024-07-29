from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genre = Genre.objects.count()
    fantasy_books = Book.objects.filter(title__icontains='Don').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'fantasy_books': fantasy_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]
    context_object_name = 'my_book_list'   # su propio nombre para la lista como variable de plantilla
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Consigue 5 libros que contengan el título de guerra.
    template_name = 'books/my_arbitrary_template_name_list.html'  # Especifique su propio nombre/ubicación de plantilla

    def get_context_data(self, **kwargs):
        # Llame primero a la implementación base para obtener un contexto.
        context = super(BookListView, self).get_context_data(**kwargs)
        # Obtenga el blog del id y agréguelo al contexto.
        context['some_data'] = 'Estos son solo algunos datos'
        return context
