package strategy;

public class Hand implements DigStrategy {
    @Override
    public void dig() {
        System.out.println("맨손으로 땅을 팝니다.");
    }
}
