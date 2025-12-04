import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from core.models import Bank, Branch


class BankNode(DjangoObjectType):
    class Meta:
        model = Bank
        interfaces = (relay.Node,)
        fields = "__all__"


class BranchNode(DjangoObjectType):
    class Meta:
        model = Branch
        interfaces = (relay.Node,)
        fields = "__all__"


class BranchConnection(relay.Connection):
    class Meta:
        node = BranchNode


class Query(graphene.ObjectType):
    branches = relay.ConnectionField(BranchConnection)

    def resolve_branches(self, info, **kwargs):
        # IMPORTANT:
        # Relay will convert queryset to edges/node format automatically
        return Branch.objects.select_related("bank").all()


schema = graphene.Schema(query=Query)
