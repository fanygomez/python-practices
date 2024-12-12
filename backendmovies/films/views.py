from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Film, FilmGenre
from .serializers import FilmSerializer, FilmGenreSerializer

# Create your views here.
class ExtendedPagination(PageNumberPagination):
    page_size = 8

    def get_paginated_response(self, data):

        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'page_size': self.page_size,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data
        })
        
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

    pagination_class = ExtendedPagination
    pagination_class.page_size = 8 # Default page size

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'
