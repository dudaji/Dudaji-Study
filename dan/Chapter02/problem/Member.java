import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public abstract class Member {
  private String date;

  public Member() {
    DateFormat dtf = new SimpleDateFormat("yyyy-MM-dd");
    final Calendar cal = Calendar.getInstance();
    cal.add(Calendar.DATE, 1);
    this.date = dtf.format(cal.getTime());
  }

  public String getDate() {
    return this.date;
  }
  
  public abstract void update(String stock, int buyPrice, int sellPrice);
}