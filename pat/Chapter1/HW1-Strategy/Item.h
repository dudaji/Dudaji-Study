#ifndef ITEM_H
#define ITEM_H

#include <string>

class Item {
public:
    Item(unsigned int id, std::string name, unsigned int cost) {
        this->id = id;
        this->name = name;
        this->cost = cost;
    }
    ~Item() {}
    unsigned int getId() { return id; }
    std::string getName() { return name; }
    unsigned int getCost() { return cost; }

private:
    unsigned int id;
    std::string name;
    unsigned int cost;
};

#endif // ITEM_H
