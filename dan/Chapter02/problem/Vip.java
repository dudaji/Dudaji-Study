public class Vip extends Member {
    private String id;
  
    public Vip(String id) {
      this.id = id;
    }
  
    @Override
    public void update(String stock, int buyPrice, int sellPrice) {
      System.out.println();
      System.out.println("---------------------------------------------------------");
      System.out.println(id+"(VIP)님만을 위한 모든 정보 제공");
      System.out.println(stock+"의 익일("+super.getDate()+") 매수/매도가");
      System.out.println("종목 : " + stock);
      System.out.println("매수가 : " + buyPrice);
      System.out.println("매도가 : " + sellPrice);
      System.out.println("---------------------------------------------------------");
    };
  }