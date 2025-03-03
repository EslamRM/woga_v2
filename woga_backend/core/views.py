from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import ContactSerializer, SupportSerializer
from .models import Support, Contact


class SupportViewSet(viewsets.ModelViewSet):
    serializer_class = SupportSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = ["subject"]
    ordering_fields = ["subject"]
    search_fields = ["subject"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {
                    "success": True,
                    "message": "Your Ticket has been submitted successfully.",
                },
                status=HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        queryset = Support.objects.filter(user=user)
        sort_by = self.request.query_params.get("sort_by")
        if sort_by:
            queryset = queryset.order_by(sort_by)
        return queryset


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "success": True,
                "message": "Your Ticket has been submitted successfully.",
            },
            status=HTTP_201_CREATED,
        )

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
