#ifndef PAY_BY_KAKAOPAY_H
#define PAY_BY_KAKAOPAY_H

#include "PayStrategy.h"

class PayByKakaoPay: public PayStrategy {
public:
    bool pay(unsigned int cost) const;
    ~PayByKakaoPay() {}
};

#endif // PAY_BY_KAKAOPAY_H
