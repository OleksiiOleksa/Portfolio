$(function() {

    /* Filter ==============*/ 
    let filter = $("[data-filter]");

    filter.on("click", function(event) {
        event.preventDefault();

        let cat = $(this).data('filter');

        if (cat == 'all') {
            $("[data-cat]").removeClass("hide");
        } else {
            $("[data-cat]").each(function() {

                let workCat = $(this).data('cat');

                if (workCat != cat) {
                    $(this).addClass('hide');
                } else {
                    $(this).removeClass('hide');
                }

            });
        }
    });

    /* Modal ==============*/

    const modalCall = $("[data-modal]"); // Элементы с атрибутом data-modal
    const modalClose = $("[data-close]"); // Элементы с атрибутом data-close
    
    // Открытие модального окна
    modalCall.on("click", function(event) {
        event.preventDefault(); // Отменяем стандартное действие

        let modalId = $(this).data('modal'); // Получаем id модального окна
        console.log("Opening modal:", modalId); // Лог для отладки

        $(modalId).addClass('show'); // Добавляем класс 'show' для отображения модального окна
        $("body").addClass('no-scroll'); // Отключаем прокрутку страницы
    });

    // Закрытие модального окна
    modalClose.on("click", function(event) {
        event.preventDefault(); // Отменяем стандартное действие

        let modalParent = $(this).closest('.modal'); // Находим родительское модальное окно
        console.log("Closing modal:", modalParent); // Лог для отладки

        modalParent.removeClass('show'); // Убираем класс 'show', чтобы скрыть модальное окно
        $("body").removeClass('no-scroll'); // Включаем прокрутку страницы
    });

     // Проверяем, если есть блок сообщений
     if ($('.messages').length) {
        // Удалить сообщение через 3 секунды
        setTimeout(function() {
            const messages = document.querySelector('.messages'); // Находим блок с сообщением
            if (messages) {
                messages.style.transition = "opacity 0.5s"; // Анимация плавного исчезновения
                messages.style.opacity = "0"; // Прозрачность на 0
                setTimeout(() => messages.remove(), 500); // Удаляем элемент через 0.5 секунды после исчезновения
            }
        }, 3000); // Задержка в 3 секунды
    }

});
