from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.shortcuts import get_object_or_404


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

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'fantasy_books': fantasy_books,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by=1
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='don')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
	model = Author
	context_object_name = 'author_list'
	paginate_by = 10


class AuthorDetailView(generic.DetailView):
	model = Author
	context_object_name = 'author'

	def get_context_data(self, **kwargs):
		context = super(AuthorDetailView, self).get_context_data(**kwargs)
		context ['author_books'] = Book.objects.filter(author=self.kwargs['pk'])
		return context

