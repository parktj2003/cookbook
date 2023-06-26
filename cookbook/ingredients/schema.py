# import 부분이 변경됩니다.
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, ObjectType, AbstractType, String

from ingredients.models import Category, Ingredient

# class 명이 변경됩니다.

class CategoryNode(DjangoObjectType):
  class Meta:
    model = Category
    filter_fields = ['name', 'ingredients']
    interfaces = (relay.Node, )

class IngredientNode(DjangoObjectType):
  class Meta:
    model = Ingredient
    # 아래와 같은 방식으로 좀 더 구체적인 필터링이 가능할 수 있습니다.

    filter_fileds = {
      'name': ['exact', 'icontains', 'istartswith'],
      'notes': ['exact', 'icontains'],
      'category': ['exact'],
      'category__name': ['exact'],
    }
    interfaces = (relay.Node, )

class Query(graphene.ObjectType):
  category = relay.Node.Field(CategoryNode)
  all_categories = DjangoFilerConnectionField(CategoryNode)

  ingredient = relay.Node.Field(IngredientNode)
  all_ingredients = DjangoFilterConnectionField(IngredientNode)


