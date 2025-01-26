from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import TodoItem
from .serializers import TodoItemSerializer





class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['completed','due_date','created_at']
    ordering_fields = ['completed','due_date', 'created_at']
    search_fields = ['title', 'description']