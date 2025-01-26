from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id','user', 'title', 'description','completed', 'due_date', 'created_at', 'updated_at']
        read_only_fields = ['id','user','created_at','updated_at']

    def validate(self, attrs):
        user = self.context.get('user')
        attrs['user'] = user
        return super().validate(attrs)