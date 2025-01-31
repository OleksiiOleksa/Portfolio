//Средняя цена
document.addEventListener("DOMContentLoaded", function () {
    const buttonGroup = document.querySelector(".button-group");
    const buttons = buttonGroup.querySelectorAll("button");
    const averagePriceValue = document.getElementById("average-price-value");

    // Функция для получения средней цены
    async function fetchAveragePrice(days) {
        averagePriceValue.textContent = "Loading...";
        try {
            const url = `/solana/average_price/?days=${days}`;  // Запрос к серверу Django
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Error fetching data: ${response.statusText}`);
            }

            const data = await response.json();
            if (data.success) {
                averagePriceValue.textContent = `${data.average_price} USD`;
            } else {
                throw new Error(data.error);
            }
        } catch (error) {
            console.error("Error fetching average price:", error);
            averagePriceValue.textContent = "Error fetching data.";
        }
    }

    // Устанавливаем активную кнопку и выполняем запрос
    function setActiveButton(button) {
        buttons.forEach((btn) => btn.classList.remove("active"));
        button.classList.add("active");
        fetchAveragePrice(button.dataset.period);
    }

    // Обработчик нажатия на кнопки
    buttons.forEach((button) => {
        button.addEventListener("click", () => setActiveButton(button));
    });

    // Загружаем данные для 7 дней по умолчанию
    fetchAveragePrice(7);
});

//Индекс страха жадности
document.addEventListener("DOMContentLoaded", function () {
    const fearGreedMeter = document.getElementById("fear-greed-meter");
    const indexValue = document.getElementById("index-greed-value");

    // Функция для получения данных индекса страха и жадности
    async function fetchFearGreedIndex() {
        try {
            const response = await fetch("https://api.alternative.me/fng/?limit=1");  // Используем другой API для Fear/Greed
            const data = await response.json();

            if (!data.data || data.data.length === 0) {
                throw new Error("No data available for Fear & Greed Index");
            }

            const index = data.data[0].value;  // Получаем значение индекса
            const maxIndex = 100;
            const minIndex = 0;

            // Проверяем, что данные корректные
            if (index === undefined || index === null) {
                throw new Error("Invalid Fear & Greed Index value");
            }

            // Обновляем отображение текста
            indexValue.textContent = `${index} (Scale: 0 - 100)`;

            // Настроим и обновим JustGage
            const fearGreedGauge = new JustGage({
                        id: "fear-greed-meter",
                        value: index,  // Индекс страха/жадности
                        min: 0,
                        max: 100,
                        title: "Fear & Greed Index",
                        label: "Max Greed",
                        levelColors: ["#f44336", "#ff9800", "#4caf50"], // Градиент от красного к зеленому
                        startAnimationTime: 3,
                        startAnimationType: ">",
                        refreshAnimationTime: 1,
                        refreshAnimationType: "bounce"
                    });

        } catch (error) {
            console.error("Error fetching Fear/Greed Index:", error);
            indexValue.textContent = "Error loading index";
        }
    }

    // Загружаем данные при загрузке страницы
    fetchFearGreedIndex();
});