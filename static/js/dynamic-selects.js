// Динамическая подгрузка категорий и подкатегорий
$(function () {
    const $type = $("#id_type");  // поле Тип
    const $category = $("#id_category");  // поле Категория
    const $subcategory = $("#id_subcategory");  // поле Подкатегория

    // Заполняет select элементами и добавляет placeholder
    function fillSelect($sel, items, placeholder) {
        $sel.empty()
            .append($("<option>").val("").text(placeholder));
        items.forEach(obj =>
            $sel.append($("<option>").val(obj.id).text(obj.name))
        );
    }

    // Загрузка категорий
    function loadCategories(typeId, keepSelected = null) {
        fillSelect($category, [], "<выберите категорию>");
        fillSelect($subcategory, [], "<выберите подкатегорию>");

        if (!typeId) return;

        $.getJSON(`/api/categories/?type=${typeId}`)
            .done(data => {
                fillSelect($category, data, "<выберите категорию>");
                if (keepSelected) $category.val(keepSelected);
            })
            .fail(err => console.error("Ошибка загрузки категорий", err));
    }

    // Загрузка подкатегорий
    function loadSubcategories(catId, keepSelected = null) {
        fillSelect($subcategory, [], "<выберите подкатегорию>");

        if (!catId) return;

        $.getJSON(`/api/subcategories/?category=${catId}`)
            .done(data => {
                fillSelect($subcategory, data, "<выберите подкатегорию>");
                if (keepSelected) $subcategory.val(keepSelected);
            })
            .fail(err => console.error("Ошибка загрузки подкатегорий", err));
    }

    // Подписка на изменения
    $type.on("change", () => loadCategories($type.val()));
    $category.on("change", () => loadSubcategories($category.val()));

    // Инициализация при открытии формы редактирования
    (function initOnLoad() {
        const initialType = $type.val();
        const initialCat = $category.val();
        const initialSub = $subcategory.val();

        if (initialType) {
            loadCategories(initialType, initialCat);
            if (initialCat) loadSubcategories(initialCat, initialSub);
        }
    })();
});