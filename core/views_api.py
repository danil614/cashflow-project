from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import (
    Status,
    RecordType,
    Category,
    SubCategory,
    CashflowRecord,
)
from .serializers import (
    StatusSerializer,
    RecordTypeSerializer,
    CategorySerializer,
    SubCategorySerializer,
    CashflowRecordSerializer,
)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class RecordTypeViewSet(viewsets.ModelViewSet):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related("type")
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type"]


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.select_related("category")
    serializer_class = SubCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class CashflowRecordViewSet(viewsets.ModelViewSet):
    queryset = CashflowRecord.objects.select_related(
        "status", "type", "category", "subcategory"
    )
    serializer_class = CashflowRecordSerializer
