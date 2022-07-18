package strategy;

public class Dudeoji {
    private CryStrategy cryStrategy;
    private DigStrategy digStrategy;

    public Dudeoji(CryStrategy cryStrategy, DigStrategy digStrategy) {
        this.cryStrategy = cryStrategy;
        this.digStrategy = digStrategy;
    }

    public void cry() {
        cryStrategy.cry();
    }

    public void dig() {
        digStrategy.dig();
    }

    public void setCryStrategy(CryStrategy cryStrategy) {
        this.cryStrategy = cryStrategy;
    }

    public void setDigStrategy(DigStrategy digStrategy) {
        this.digStrategy = digStrategy;
    }
}

