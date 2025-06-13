from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField("Статус", max_length=64, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self) -> str:
        return self.name


class RecordType(models.Model):
    name = models.CharField("Тип", max_length=64, unique=True)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    type = models.ForeignKey(
        RecordType,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Тип",
    )
    name = models.CharField("Категория", max_length=64)

    class Meta:
        unique_together = ("type", "name")
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория",
    )
    name = models.CharField("Подкатегория", max_length=64)

    class Meta:
        unique_together = ("category", "name")
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self) -> str:
        return self.name


class CashflowRecord(models.Model):
    created_at = models.DateField(
        "Дата",
        default=timezone.now,  # подставляет текущую дату
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey(RecordType, on_delete=models.PROTECT, verbose_name="Тип")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.PROTECT, verbose_name="Подкатегория"
    )
    amount = models.DecimalField("Сумма, ₽", max_digits=12, decimal_places=2)
    comment = models.TextField("Комментарий", blank=True, default="")

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ("-created_at", "id")

    # бизнес-валидация
    def clean(self) -> None:
        errors = {}

        # подкатегория обязательна
        if not self.subcategory_id:
            errors["subcategory"] = "Подкатегория обязательна."

        # связь подкатегория - категория
        elif self.subcategory.category_id != self.category_id:
            errors["subcategory"] = (
                "Подкатегория не относится к выбранной категории."
            )

        # связь категория - тип
        if (
                self.category_id
                and self.type_id
                and self.category.type_id != self.type_id
        ):
            errors["category"] = (
                "Категория не относится к выбранному типу."
            )

        if errors:
            raise ValidationError(errors)

    def __str__(self) -> str:
        return f"{self.created_at} · {self.amount}₽"
