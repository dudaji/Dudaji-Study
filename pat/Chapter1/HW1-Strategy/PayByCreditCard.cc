#include <iostream>
#include "PayByCreditCard.h"

bool PayByCreditCard::pay(unsigned int cost) const
{
    /*
    CreditCard card = CreditCard(cardNumber, expireDate, cvc);
    if (!card.isValid()) {
        std::cerr << "Wanna goto jail?" << '\n';
        return false;
    }
    card.pay(cost);
    return true;
    */
    std::cout << "CreditCard: " << cost << '\n';
    return true;
}
