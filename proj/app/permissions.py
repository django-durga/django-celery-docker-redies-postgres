from rest_framework import permissions


from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.permissions import BasePermission


class IsAllowedToRead(BasePermission):
     def has_permission(self, request, view):
         s=User.objects.filter(username=str(request.user.username))
         for r in s:
             return str(r.is_staff)== 'True'