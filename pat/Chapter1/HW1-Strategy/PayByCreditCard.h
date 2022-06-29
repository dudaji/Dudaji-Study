#ifndef PAY_BY_CREDIT_CARD_H
#define PAY_BY_CREDIT_CARD_H

#include "PayStrategy.h"

class PayByCreditCard: public PayStrategy {
public:
    bool pay(unsigned int cost) const;
    ~PayByCreditCard() {}
};

#endif // PAY_BY_CREDIT_CARD_H
