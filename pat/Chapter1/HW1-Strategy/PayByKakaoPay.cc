#include <iostream>
#include "PayByKakaoPay.h"

bool PayByKakaoPay::pay(unsigned int cost) const
{
    /* 
    kakaoPayAccount = KakaoPayLogin();
    balance = kakaoPayAccount.getBalance();
    if (balance < cost) {
        std::cerr << "Show me the money" << '\n';
        return false;
    }
    kakaoPayAccount.setBalance(balance - cost);
    return true;
    */
    std::cout << "KakaoPay: " << cost << '\n';
    return true;
}
