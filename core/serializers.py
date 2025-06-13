from rest_framework import serializers

from .models import (
    Status,
    RecordType,
    Category,
    SubCategory,
    CashflowRecord,
)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class RecordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordType
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CashflowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashflowRecord
        fields = "__all__"

    # дублируем бизнес-валидацию для API
    def validate(self, data):
        category = data["category"]
        subcategory = data["subcategory"]
        record_type = data["type"]

        if category.type_id != record_type.id:
            raise serializers.ValidationError(
                {"category": "Selected category does not belong to selected type."}
            )
        if subcategory.category_id != category.id:
            raise serializers.ValidationError(
                {"subcategory": "Selected subcategory does not belong to selected category."}
            )
        return data
