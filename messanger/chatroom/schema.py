import graphene
from graphene_django import DjangoObjectType
from pkg_resources import require
from .models import Chatroom, Message, Member

# Objecttypes
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

# Query class
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

# InputObjectTypes
class ChatroomInput(graphene.InputObjectType):
    cname = graphene.String()

class MemberInput(graphene.InputObjectType):
    mname = graphene.String()

# Mutation class
class CreateChatroom(graphene.Mutation):
    class Arguments:
        input=ChatroomInput(required=True)
    
    chatroom=graphene.Field(ChatroomType)
    
    def mutate(root, info, input):
        cr = Chatroom()
        cr.cname=input.cname
        cr.save()
        return CreateChatroom(chatroom=cr)

class CreateMember(graphene.Mutation):
    class Arguments:
        input=MemberInput(required=True)
    
    member=graphene.Field(MemberType)
    
    def mutate(root, info, input):
        m = Member()
        m.mname=input.mname
        m.save()
        return CreateMember(member=m)

class Mutation(graphene.ObjectType):
    create_chatroom=CreateChatroom.Field()
    create_member=CreateMember.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
