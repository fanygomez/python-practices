from rest_framework import viewsets, filters, status, views, authentication, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Film, FilmGenre, FilmUser
from .serializers import FilmSerializer, FilmGenreSerializer, FilmUserSerializer

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
    ordering_fields = ['title', 'year', 'genres__name', 'favorites', 'average_note']
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

class FilmUserViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        queryset = FilmUser.objects.filter(user=self.request.user)
        serializer = FilmUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        try:
            film = Film.objects.get(id=request.data['uuid'])
        except Film.DoesNotExist:
            return Response(
                {'status': 'Film not found'},
                status=status.HTTP_404_NOT_FOUND)

        film_user, created = FilmUser.objects.get_or_create(user=request.user, film=film)
        
        film_user.state = request.data.get('state', 0)
        film_user.favorite = request.data.get('favorite', False)
        film_user.note = request.data.get('note', -1)
        film_user.review = request.data.get('review', None)
        
        if created == False:
            return Response({'status': 'Exists'}, status=status.HTTP_400_BAD_REQUEST)
            
        # If the movie is marked as NOT VIEWED we automatically delete it.
        if int(film_user.state) == 0:
            film_user.delete()
            return Response(
                {'status': 'Deleted'}, status=status.HTTP_200_OK)

        # En otro caso guardamos los campos de la película de usuario
        else:
            film_user.save()

        return Response({'status': 'Saved'}, status=status.HTTP_201_CREATED)