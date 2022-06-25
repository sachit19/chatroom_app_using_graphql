import graphene
from graphene_django import DjangoObjectType
from .models import Chatroom, Message, Member

# Graphene objecttypes
class ChatroomType(DjangoObjectType):
    class Meta: 
        model = Chatroom
        fields = ('id','cname')

class MemberType(DjangoObjectType):
    class Meta: 
        model = Member
        fields = ('id','mname')

class MessageType(DjangoObjectType):
    class Meta: 
        model = Message
        fields = ('id','msg','member','chatroom','created_at')

# Graphene query class
class Query(graphene.ObjectType):
    chatrooms = graphene.List(ChatroomType)
    members = graphene.List(MemberType)
    messages = graphene.List(MessageType)

    def resolve_members(root, info, **kwargs):
        # Querying a list
        return Member.objects.all()

    def resolve_chatrooms(root, info, **kwargs):
        # Querying a list
        return Chatroom.objects.all()

    def resolve_messages(root, info, **kwargs):
        # Querying a list
        return Message.objects.all()


schema = graphene.Schema(query=Query)
