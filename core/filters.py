import django_filters
from django import forms

from .models import CashflowRecord


class CashflowRecordFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(
        field_name="created_at", lookup_expr="gte", label="Дата от",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    created_at__lte = django_filters.DateFilter(
        field_name="created_at", lookup_expr="lte", label="Дата до",
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = CashflowRecord
        fields = ["status", "type", "category", "subcategory"]
