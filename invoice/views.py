from rest_framework import generics
from .models import Invoice
from .serializers import InvoiceSerializer

# List & Create Invoice
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# Retrieve, Update & Delete Invoice
class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_number"  # Use invoice_number as the lookup key
