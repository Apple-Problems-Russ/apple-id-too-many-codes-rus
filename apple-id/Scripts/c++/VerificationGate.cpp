#include <iostream>
#include <string>
#include <chrono>
#include <map>

struct SecurityProfile {
    int requestCount;
    std::chrono::steady_clock::time_point lastRequestTime;
};

class SmsGateway {
private:
    std::map<std::string, SecurityProfile> rateLimiter;
    const int maxRequests = 3;

public:
    bool SendSms(const std::string& phoneNumber, const std::string& code) {
        auto now = std::chrono::steady_clock::now();
        auto& profile = rateLimiter[phoneNumber];

        // Проверка жесткого лимита запросов
        if (profile.requestCount >= maxRequests) {
            std::cout << "CRITICAL: Gateway blocked for " << phoneNumber << ". Rate limit reached." << std::endl;
            return false;
        }

        profile.requestCount++;
        profile.lastRequestTime = now;
        
        std::cout << "SUCCESS: Packet sent to +7 network. Payload: " << code << std::endl;
        return true;
    }
};

int main() {
    SmsGateway gateway;
    std::string phone = "+79991234567";
    
    for (int i = 0; i < 4; ++i) {
        gateway.SendSms(phone, "482019");
    }
    return 0;
}

