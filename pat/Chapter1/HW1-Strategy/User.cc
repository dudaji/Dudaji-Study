#include <iostream>
#include "User.h"
#include "Item.h"

bool User::addItemToShoppingList(Item item)
{
    shoppingList.push_back(item);
    totalCost += item.getCost();
    return true;
}

bool User::clearShoppingList()
{
    shoppingList.clear();
    totalCost = 0;
    return true;
}

bool User::payment()
{
	if (payStrategy == nullptr) {
        // Don't pay
        return true;
    }
    bool result = payStrategy->pay(totalCost);
    if (result == false) {
        std::cerr << "Payment failed" << '\n';
        return false;
    }
    clearShoppingList();
    return true;
}
