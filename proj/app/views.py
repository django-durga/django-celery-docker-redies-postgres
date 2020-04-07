from .models import Customer
from django.contrib.auth.models import User
from .serializers import Customerializer,UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from .permissions import IsAllowedToRead
from .tasks import send_mail
from .serializers import MailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
subject, sender = 'durgaPrasadDjangoDemo', 'durgaprasad@gmail.com'
html_content='<h2>You are registered as a customer in durgaDjangoDemo</h2>'


class UserList(generics.ListCreateAPIView):
    #permission_classes = [IsAllowedToRead,]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Customer.objects.all()
    serializer_class = Customerializer


class CustomerCreate(APIView):
    permission_classes = [IsAllowedToRead, IsAuthenticated]
    def post(self,request):
        serializer = Customerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data=request.data
            email=data['email']
            try:
               if (('@' not in email) or ('.' not in email)):
                   raise Exception
               result = send_mail(subject, sender, email, html_content)
               if result == 'success':
                pass

               else:
                raise Exception
            except:
              return Response('Error in sending mail')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetails(APIView):
    permission_classes = [IsAllowedToRead, IsAuthenticated]
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



