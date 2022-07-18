package extend;

public class GreenDudeoji extends Dudeoji {
    @Override
    public void display() {
        System.out.println("초록색 두더지입니다.");
    }
    @Override
    public void dig() {
        System.out.println("맨손으로 땅을 팝니다.");
    }
}
