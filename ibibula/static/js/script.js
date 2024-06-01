document.getElementById('categories').addEventListener('change', function () {
    var subcategories = document.getElementById('subcategories');
    if (this.value === 'Ремонт') {
        subcategories.style.display = 'block';
    } else {
        subcategories.style.display = 'none';
    }
});