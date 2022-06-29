#ifndef USER_H
#define USER_H

#include <vector>
#include "Item.h"
#include "PayStrategy.h"

class User {
public:
    User() {
        this->payStrategy = nullptr;
        this->shoppingList.clear();
        this->totalCost = 0;
    }
    User(PayStrategy* payStrategy) {
        this->payStrategy = payStrategy;
        this->shoppingList.clear();
        this->totalCost = 0;
    }

    ~User() {
        if (payStrategy) delete payStrategy;
    }

    void setPaymentStrategy(PayStrategy* payStrategy) {
				if (this->payStrategy != nullptr)
					delete this->payStrategy;
        this->payStrategy = payStrategy;
    }
    
    bool payment();
    bool addItemToShoppingList(Item item);
    bool clearShoppingList();

private:
    PayStrategy* payStrategy;
    std::vector<Item> shoppingList;
    unsigned int totalCost;
};

#endif // USER_H
