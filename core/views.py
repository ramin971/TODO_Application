from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import TodoItem
from .serializers import TodoItemSerializer





class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['completed','due_date','created_at']
    ordering_fields = ['completed','due_date', 'created_at']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)
    

    def get_serializer_context(self):
        return {'user':self.request.user}