import time
import random

class AppleIDAuthSystem:
    def __init__(self):
        self.max_attempts = 3
        self.cooldown_period = 86400  # 24 часа в секундах
        self.user_database = {
            "user@gmail.com": {
                "phone": "+79991234567",
                "attempts": 0,
                "last_attempt_time": 0,
                "valid_code": None
            }
        }

    def request_verification_code(self, email: str) -> str:
        current_time = time.time()
        user = self.user_database.get(email)
        
        if not user:
            return "ERROR: User not found"

        # Проверка временного лимита блокировки
        if user["attempts"] >= self.max_attempts:
            if current_time - user["last_attempt_time"] < self.cooldown_period:
                return "ERROR: Too many codes sent. Limit exceeded. Wait 24 hours."
            else:
                user["attempts"] = 0  # Сброс лимита по истечении суток

        # Генерация нового 6-значного кода
        generated_code = str(random.randint(100000, 999999))
        user["valid_code"] = generated_code
        user["attempts"] += 1
        user["last_attempt_time"] = current_time
        
        # Симуляция отправки через шлюз
        print(f"SMS Gateway: Code {generated_code} sent to {user['phone']}")
        return "SUCCESS: Code sent"

    def verify_code(self, email: str, input_code: str) -> bool:
        user = self.user_database.get(email)
        if user and user["valid_code"] == input_code:
            user["attempts"] = 0  # Успешный вход сбрасывает счетчик ошибок
            user["valid_code"] = None
            return True
        return False

# Инициализация и тест лимита
auth_system = AppleIDAuthSystem()
for _ in range(4):
    print(auth_system.request_verification_code("user@gmail.com"))
  
