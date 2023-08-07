from django.shortcuts import render
from django.views import generic
from .models import Book
from .models import Book, Author,BookInstance

def FstTmpView(request):
    """View function for the home page of the site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # Your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='a')[:5]  # Get 5 books containing the title with 'a'
    template_name = 'BookStoreApp/books/author_list.html'  # Specify your own template name/location

    paginate_by = 10  # Pagination

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
