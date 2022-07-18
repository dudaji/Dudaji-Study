package strategy;

public class Drill implements DigStrategy {
    @Override
    public void dig() {
        System.out.println("드릴로 땅을 팝니다.");
    }
}
