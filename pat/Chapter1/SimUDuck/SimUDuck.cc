#include <iostream>
#include "SimUDuck.h"

void FlyWithWings::fly() const
{
    std::cout << "Fly high!" << '\n';
}

void FlyNoWay::fly() const
{
    std::cout << "I can't fly!" << '\n';
}

void Quack::quack() const
{
    std::cout << "Quack!" << '\n';
}

void Squeak::quack() const
{
    std::cout << "Squeak!" << '\n';
}

void MuteQuack::quack() const
{
    std::cout << "..." << '\n';
}

void Duck::swim() const
{
    std::cout << "Swim!" << '\n';
}

class MallardDuck: public Duck {
public:
    MallardDuck(): Duck(new FlyWithWings(), new Quack()) { }
    void display() const {
        std::cout << "This is MallardDuck" << '\n';
    }
};

class RubberDuck: public Duck {
public:
    RubberDuck(): Duck(new FlyNoWay(), new Squeak()) { }
    void display() const {
        std::cout << "This is RubberDuck" << '\n';
    }
};

int main()
{
    MallardDuck* mallard = new MallardDuck();
    RubberDuck* rubberduck = new RubberDuck();

    mallard->display();
    mallard->performFly();
    mallard->performQuack();
    mallard->swim();

    rubberduck->display();
    rubberduck->performFly();
    rubberduck->performQuack();
    rubberduck->swim();

    return 0;
}
