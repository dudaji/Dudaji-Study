class FlyBehavior {
public:
    virtual void fly() const = 0;
    virtual ~FlyBehavior() {}
};

class QuackBehavior {
public:
    virtual void quack() const = 0;
    virtual ~QuackBehavior() {}
};

class Duck {
public:
    Duck(FlyBehavior* flyBehavior, QuackBehavior* quackBehavior) {
        this->flyBehavior = flyBehavior;
        this->quackBehavior = quackBehavior;
    }
    ~Duck() {
        if (flyBehavior) delete flyBehavior;
        if (quackBehavior) delete quackBehavior;
    }
    void performQuack() {
        quackBehavior->quack();
    }

    void performFly() {
        flyBehavior->fly();
    }

    void swim() const;
    virtual void display() const = 0;

protected:
    FlyBehavior* flyBehavior;
    QuackBehavior* quackBehavior;
};

class FlyWithWings: public FlyBehavior {
public:
    void fly() const;
    ~FlyWithWings() {}
};

class FlyNoWay: public FlyBehavior {
public:
    void fly() const;
    ~FlyNoWay() {}
};

class Quack: public QuackBehavior {
public:
    void quack() const;
    ~Quack() {}
};

class Squeak: public QuackBehavior {
public:
    void quack() const;
    ~Squeak() {}
};

class MuteQuack: public QuackBehavior {
public:
    void quack() const;
    ~MuteQuack() {}
};
