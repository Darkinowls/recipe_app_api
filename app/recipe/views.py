from django.db.models import QuerySet
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core import models
from recipe import serializers


# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset: QuerySet = models.Recipe.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        recipes = self.queryset.filter(user=self.request.user)
        return recipes.order_by("-id")

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "list":
            return serializers.RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer: serializers.RecipeSerializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)


class TagViewSet(mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.TagSerializer
    queryset: QuerySet = models.Tag.objects.all()

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by("-name")