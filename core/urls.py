from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views_html as html
from .views_api import (
    StatusViewSet,
    RecordTypeViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    CashflowRecordViewSet,
)

router = DefaultRouter()
router.register(r"api/statuses", StatusViewSet)
router.register(r"api/types", RecordTypeViewSet)
router.register(r"api/categories", CategoryViewSet)
router.register(r"api/subcategories", SubCategoryViewSet)
router.register(r"api/records", CashflowRecordViewSet)

app_name = "records"

urlpatterns = [
    # HTML
    path("", html.CashflowListView.as_view(), name="list"),
    path("new/", html.CashflowCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", html.CashflowUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", html.CashflowDeleteView.as_view(), name="delete"),
    path(
        "dictionaries/",
        html.DictionariesManageView.as_view(),
        name="dictionaries-manage",
    ),
    # API
    *router.urls,
]
