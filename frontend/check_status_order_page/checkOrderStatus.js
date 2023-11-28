document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const orderInfo = document.getElementById('orderInfo');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const orderNumber = document.getElementById('orderNumber').value;

        // Отправка запроса на сервер
        const response = await fetch(`/api/clients/order_number/${orderNumber}`);
        const data = await response.json();

        // Обновление данных о заказе на странице
        orderInfo.innerHTML = `
            <span>Статус заказа: ${data.status}</span>
            <span>Дата окончания строительства: ${data.due_date}</span>
            <span>Дата создания заказа: ${data.created_at}</span>
            <span>Бюджет: ${data.budget}</span>
            <span>Тип дома: ${data.type_of_house}</span>
            <span>Количество этажей: ${data.num_floors}</span>
            <span>Квадратура дома: ${data.square_of_house}</span>
        `;
    });
});
