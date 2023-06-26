import graphene
import cookbook.ingredients.schema

from graphene_django.debug import DjangoDebug


#class Query(
#    ingredients.schema.Query,
#    graphene.ObjectType,
#):
#    debug = graphene.Field(DjangoDebug, name="_debug")

class Query(cookbook.ingredients.schema.Query, graphene.ObjectType,):
    pass


schema = graphene.Schema(query=Query)