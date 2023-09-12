from contacts.models import Contacts
from .serializers import ContactsSerializer
from rest_framework import viewsets, permissions


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contacts.objects.filter(user=self.request.user).order_by("id")
