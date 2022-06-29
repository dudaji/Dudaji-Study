#include <iostream>
#include "User.h"
#include "Item.h"
#include "PayByKakaoPay.h"
#include "PayByCreditCard.h"

int main(void)
{
    User* user = new User();
    
    user->setPaymentStrategy(new PayByKakaoPay());
    user->addItemToShoppingList(Item(1, "Coke", 2000));
    user->addItemToShoppingList(Item(2, "Coffee", 5000));
    user->payment();

    user->setPaymentStrategy(new PayByCreditCard());
    user->addItemToShoppingList(Item(3, "Pen", 1000));
    user->addItemToShoppingList(Item(4, "Eraser", 500));
    user->payment();
    return 0;
}
