document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('categories');
    const subcategorySelect = document.getElementById('subcategories');
    const subcatOptions = Array.from(document.querySelectorAll('.subcat-option'));
    const services = Array.from(document.querySelectorAll('.service-card'));
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('service-search');
    const paginationContainer = document.getElementById('pagination');
    const itemsPerPage = 10;
    let currentPage = 1;
    let filteredServices = [];

    function renderServices(page = 1) {
        const start = (page - 1) * itemsPerPage;
        const end = start + itemsPerPage;
        services.forEach((service, index) => {
            if (filteredServices.includes(service)) {
                service.style.display = (filteredServices.indexOf(service) >= start && filteredServices.indexOf(service) < end) ? 'flex' : 'none';
            } else {
                service.style.display = 'none';
            }
        });
        console.log(`Rendered services for page ${page}`);
    }

    function renderPagination() {
        paginationContainer.innerHTML = '';
        const pageCount = Math.ceil(filteredServices.length / itemsPerPage);
        if (pageCount <= 1) return; // Если одна страница или меньше, не отображаем пагинацию
        for (let i = 1; i <= pageCount; i++) {
            const pageButton = document.createElement('button');
            pageButton.innerText = i;
            pageButton.addEventListener('click', function () {
                currentPage = i;
                renderServices(i);
            });
            paginationContainer.appendChild(pageButton);
        }
        console.log('Pagination rendered with', pageCount, 'pages');
    }

    function filterServices() {
        const selectedCategory = categorySelect.value;
        const selectedSubcategory = subcategorySelect.value;
        const searchTerm = searchInput.value.toLowerCase();

        filteredServices = services.filter(service => {
            const serviceCategory = service.getAttribute('data-category');
            const serviceSubcategory = service.getAttribute('data-subcategory');
            const serviceName = service.querySelector('.body-text').textContent.toLowerCase();

            return (selectedCategory === "" || serviceCategory === selectedCategory) &&
                   (selectedSubcategory === "" || serviceSubcategory === selectedSubcategory) &&
                   (searchTerm === "" || serviceName.includes(searchTerm));
        });

        currentPage = 1;
        renderServices();
        renderPagination();
        console.log('Services filtered, total:', filteredServices.length);
    }

    categorySelect.addEventListener('change', function () {
        const categoryId = this.value;

        if (categoryId === "") {
            subcategorySelect.style.display = 'none';
            subcategorySelect.value = "";
        } else {
            subcategorySelect.style.display = 'block';
        }

        subcatOptions.forEach(option => {
            const optionCategories = option.dataset.category.split(',');
            if (optionCategories.includes(categoryId) || categoryId === "") {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });

        filterServices();
    });

    subcategorySelect.addEventListener('change', filterServices);
    searchButton.addEventListener('click', filterServices);
    searchInput.addEventListener('input', filterServices);

    filterServices();
});
