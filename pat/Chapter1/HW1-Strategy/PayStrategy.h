#ifndef PAY_STRATEGY_H
#define PAY_STRATEGY_H

class PayStrategy {
public:
    virtual bool pay(unsigned int cost) const = 0;
    virtual ~PayStrategy() {}
};

#endif // PAY_STRATEGY_H
