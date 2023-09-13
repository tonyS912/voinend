from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .serializers import ContactsSerializer
from contacts.models import Contacts


class ContactView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        contacts_items = Contacts.objects.all()
        serializer_class = ContactsSerializer(contacts_items, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = ContactsSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class ContactDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, id):
        contact = Contacts.objects.get(id=id)
        serializer_class = ContactsSerializer(contact)
        return Response(serializer_class.data)

    # alle daten zum ändern nötig auch unveränderte
    def put(self, request, id):
        contact = Contacts.objects.get(id=id)
        serializer_class = ContactsSerializer(contact, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Contacts.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
