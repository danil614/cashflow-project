from django.contrib import admin

from .models import (
    Status,
    RecordType,
    Category,
    SubCategory,
    CashflowRecord,
)

admin.site.register(Status)
admin.site.register(RecordType)
admin.site.register(Category)
admin.site.register(SubCategory)


@admin.register(CashflowRecord)
class CashflowRecordAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "amount",
        "status",
        "type",
        "category",
        "subcategory",
    )
    list_filter = ("status", "type", "category", "subcategory")
