// taskmanager/static/js/taskmanager.js

document.addEventListener('DOMContentLoaded', function () {
    const toggleStatusButtons = document.querySelectorAll('.toggle-status');

    toggleStatusButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const taskId = this.dataset.taskId;
            const statusElement = this.previousElementSibling;

            fetch(`/tasks/update/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'Completed') {
                    statusElement.textContent = 'Completed';
                    this.textContent = 'Mark as Not Completed';
                } else {
                    statusElement.textContent = 'Not Completed';
                    this.textContent = 'Mark as Completed';
                }
            });
        });
    });
});
