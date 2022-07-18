public class Normal extends Member {
    private String id;
  
    public Normal(String id) {
      this.id = id;
    }
  
    @Override
    public void update(String stock, int buyPrice, int sellPrice) {
      System.out.println();
      System.out.println("---------------------------------------------------------");
      System.out.println(id+"님! 회원제에 가입하셔서 VIP가 되시면 모든 정보를 이용하실 수 있습니다.");
      System.out.println(stock+"의 익일("+super.getDate()+") 매수가");
      System.out.println("종목 : " + stock);
      System.out.println("매수가 : " + buyPrice);
      System.out.println("---------------------------------------------------------");
    };
  }