from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from .filters import CashflowRecordFilter
from .forms import CashflowRecordForm
from .models import (
    CashflowRecord,
    Status,
    RecordType,
    Category,
    SubCategory,
)


class CashflowListView(ListView):
    model = CashflowRecord
    template_name = "records/list.html"
    paginate_by = 30

    def get_queryset(self):
        qs = super().get_queryset().select_related(
            "status", "type", "category", "subcategory"
        )
        self.filterset = CashflowRecordFilter(self.request.GET, queryset=qs)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filterset"] = self.filterset
        return ctx


class CashflowCreateView(CreateView):
    model = CashflowRecord
    form_class = CashflowRecordForm
    template_name = "records/form.html"
    success_url = reverse_lazy("records:list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно добавлена.")
        return super().form_valid(form)


class CashflowUpdateView(UpdateView):
    model = CashflowRecord
    form_class = CashflowRecordForm
    template_name = "records/form.html"
    success_url = reverse_lazy("records:list")

    def form_valid(self, form):
        messages.success(self.request, "Изменения сохранены.")
        return super().form_valid(form)


class CashflowDeleteView(DeleteView):
    model = CashflowRecord
    template_name = "records/form.html"
    success_url = reverse_lazy("records:list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Запись удалена.")
        return super().delete(request, *args, **kwargs)


class DictionariesManageView(TemplateView):
    template_name = "dictionaries/manage.html"

    def post(self, request, *args, **kwargs):
        # CRUD справочников можно реализовать аналогично
        messages.info(request, "Изменения в справочниках сохранены.")
        return redirect("records:dictionaries-manage")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "statuses": Status.objects.all(),
                "types": RecordType.objects.all(),
                "categories": Category.objects.select_related("type"),
                "subcategories": SubCategory.objects.select_related("category"),
            }
        )
        return ctx
