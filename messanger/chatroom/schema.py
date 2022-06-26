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
        return Member.objects.all()

    def resolve_chatrooms(root, info, **kwargs):
        return Chatroom.objects.all()

    def resolve_messages(root, info, **kwargs):
        return Message.objects.all()

# InputObjectTypes
class ChatroomInput(graphene.InputObjectType):
    cname = graphene.String()

class MemberInput(graphene.InputObjectType):
    mname = graphene.String()

class MessageInput(graphene.InputObjectType):
    msg=graphene.String()
    member=graphene.String()
    chatroom=graphene.String()

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

class CreateMessage(graphene.Mutation):
    class Arguments:
        input=MessageInput(required=True)
    
    message=graphene.Field(MessageType)
    
    def mutate(root, info, input):
        message = Message()
        message.msg=input.msg
        message.chatroom=Chatroom.objects.get(cname=input.chatroom)
        message.member=Member.objects.get(mname=input.member)
        message.save()
        return CreateMessage(message=message)

class Mutation(graphene.ObjectType):
    create_chatroom=CreateChatroom.Field()
    create_member=CreateMember.Field()
    create_message=CreateMessage.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
