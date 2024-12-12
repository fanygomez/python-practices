from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Film, FilmGenre
from .serializers import FilmSerializer, FilmGenreSerializer

# Create your views here.

class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
    filter_backends = [DjangoFilterBackend,  filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'year', 'genres__name']
    ordering_fields = ['title', 'year', 'genres__name']
    filterset_fields = {
        'year': ['lte', 'gte'],  # year is less than or equal to, year is greater than or equal to
        'genres': ['exact']
    }

    pagination_class = PageNumberPagination
    pagination_class.page_size = 8 # Default page size

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'
