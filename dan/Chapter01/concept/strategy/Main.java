package strategy;

public class Main {
    public static void main(String[] args) {
        Dudeoji dudeoji = new Dudeoji(new Kkik(), new Hand());
        dudeoji.cry();
        dudeoji.dig();

        dudeoji.setCryStrategy(new Bbak());
        dudeoji.setDigStrategy(new Drill());
    }
}