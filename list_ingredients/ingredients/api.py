from ingredients.models import Ingredient
from rest_framework import viewsets, permissions
from ingredients.serializers import IngredientSerializer

# Collect all Ingredient objects
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IngredientSerializer
    