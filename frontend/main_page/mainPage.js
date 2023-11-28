document.addEventListener("DOMContentLoaded", function () {
    let orderForm = document.querySelector(".orderBox");
    let errorMessage = document.querySelector(".errorMessage");
    let successMessage = document.querySelector(".successMessage");

    if (orderForm) {
        orderForm.addEventListener("submit", function (event) {
            event.preventDefault();

            let formData = {
                first_name: document.querySelector(".inputName input").value,
                last_name: document.querySelector(".inputSurname input").value,
                email: document.querySelector(".inputemail input").value,
                phone_number: document.querySelector(".inputPhone input").value,
                type_of_house: document.querySelector(".inputType input").value,
                num_floors: document.querySelector(".inputFloors input").value,
                square_of_house: document.querySelector(".inputSquare input").value,
                budget: document.querySelector(".inputBudget input").value,
                status: "In pending",
                created_at: new Date().toISOString().split('T')[0],
                due_date: new Date().toISOString().split('T')[0]
            };

            fetch("/api/clients/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            })
            .then(response => {
                if (!response.ok) {
                    if (response.status === 422) {
                        throw new Error("Форма заполнена неверно. Пожалуйста, проверьте введенные данные.");
                    } else {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                // Действия после успешного создания заказа
                successMessage.textContent = `Заказ успешно добавлен! Ваш номер заказа: ${data.order_number}`;
                successMessage.style.display = "block";
                successMessage.classList.add("success-message"); // Добавляем класс
            })
            .catch(error => {
                console.error(error);
                // Действия в случае ошибки
                errorMessage.textContent = error.message;
                errorMessage.style.color = "red";
                errorMessage.style.display = "block";
                errorMessage.classList.remove("success-message"); // Убираем класс
            });
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var navigationMenu = document.querySelector('.navigationMenu');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) {
            navigationMenu.classList.add('scrolled');
        } else {
            navigationMenu.classList.remove('scrolled');
        }
    });
});
