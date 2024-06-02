document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('categories');
    const subcategorySelect = document.getElementById('subcategories');
    const subcatOptions = document.querySelectorAll('.subcat-option');

    categorySelect.addEventListener('change', function () {
        const categoryId = this.value;

        if (categoryId === "") {
            subcategorySelect.style.display = 'none';
        } else {
            subcategorySelect.style.display = 'block';
        }

        subcatOptions.forEach(option => {
            if (option.dataset.category === categoryId || categoryId === "") {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });
    });
});