document.addEventListener("DOMContentLoaded", function() {
    const cancelLinks = document.querySelectorAll("a[href*='cancel_dish_order']");

    cancelLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            if (!confirm("Bạn có chắc chắn muốn hủy món ăn này không?")) {
                event.preventDefault();
            }
        });
    });
});
