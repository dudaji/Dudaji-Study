class Main {
    public static void main(String[] args) {
        Notificator notificator = new Notificator("삼성전자", 1000, 1100);

        notificator.stockManager.subscribe("vip", new Vip("vipUser"));
        notificator.stockManager.subscribe("vip", new Vip("vipUser2"));
        notificator.stockManager.subscribe("normal", new Normal("normalUser"));
        notificator.stockManager.subscribe("normal", new Normal("normalUser2"));

        try {
          notificator.normal();
          notificator.vip();  
        } catch (Exception e) {
          System.out.println(e);
        }
        
    }
}