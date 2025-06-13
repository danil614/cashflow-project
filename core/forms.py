from django import forms

from .models import CashflowRecord, Category, SubCategory


class CashflowRecordForm(forms.ModelForm):
    created_at = forms.DateField(
        label="Дата",
        widget=forms.DateInput(
            attrs={"type": "date"},
            format="%Y-%m-%d",  # то, что появится в value
        ),
        input_formats=["%Y-%m-%d"],  # то, что принимает сервер
    )

    class Meta:
        model = CashflowRecord
        fields = (
            "created_at",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        )
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # динамическая фильтрация списков
        data = self.data or None

        if data and data.get("type"):
            self.fields["category"].queryset = Category.objects.filter(
                type_id=data["type"]
            )
        elif self.instance.pk:
            self.fields["category"].queryset = Category.objects.filter(
                type=self.instance.type
            )

        if data and data.get("category"):
            self.fields["subcategory"].queryset = SubCategory.objects.filter(
                category_id=data["category"]
            )
        elif self.instance.pk:
            self.fields["subcategory"].queryset = SubCategory.objects.filter(
                category=self.instance.category
            )
