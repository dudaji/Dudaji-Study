public class Notificator {
    public StockManager stockManager;
    private String stock;
    private int buyPrice;
    private int sellPrice;

    public Notificator(String stock, int buyPrice, int sellPrice) {
        this.stockManager = new StockManager("normal", "vip");
        this.buyPrice = buyPrice;
        this.sellPrice = sellPrice;
        this.stock = stock;
    }

    public void normal() {
        stockManager.notify("normal", this.stock, this.buyPrice, this.sellPrice);
    }

    public void vip() {
        stockManager.notify("vip", this.stock, this.buyPrice, this.sellPrice);
    }
}
