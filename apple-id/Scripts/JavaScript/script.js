document.getElementById('authForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const codeField = document.getElementById('codeField');
    const errorBanner = document.getElementById('errorBanner');
    const inputCode = codeField.value.trim();

    // Базовая проверка структуры
    if (inputCode.length !== 6 || isNaN(inputCode)) {
        alert('Введите корректный 6-значный цифровой код.');
        return;
    }

    // Имитация ответа от сервера со сброшенным лимитом
    const serverResponse = {
        status: "ERROR_LIMIT_EXCEEDED",
        message: "Too many codes sent"
    };

    if (serverResponse.status === "ERROR_LIMIT_EXCEEDED") {
        errorBanner.style.display = "block";
        codeField.style.borderColor = "#ff3b30";
    }
});

document.getElementById('recoveryBtn').addEventListener('click', function(event) {
    event.preventDefault();
    console.log("Redirecting user to account recovery pipeline via Gmail validation.");
});


