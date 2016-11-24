# cookbook/ingredients/schema.py
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Project, Sprint, Task


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class ProjectNode(DjangoObjectType):
    class Meta:
        model = Project
        filter_fields = ['name', 'status']
        interfaces = (relay.Node, )


class Query(AbstractType):
    project = relay.Node.Field(ProjectNode)
    projects = DjangoFilterConnectionField(ProjectNode)
