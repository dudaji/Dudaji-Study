import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StockManager {
    Map<String, List<Member>> listeners = new HashMap<>();

    public StockManager(String... memberships) {
        for (String membership : memberships) {
            this.listeners.put(membership, new ArrayList<>());
        }
    }

    public void subscribe(String membership, Member member) {
        List<Member> members = listeners.get(membership);
        members.add(member);
    }

    public void deSubscribe(String membership, Member member) {
        List<Member> members = listeners.get(membership);
        members.remove(member);
    }

    public void notify(String membership, String stock, int buyPrice, int sellPrice) {
        List<Member> members = listeners.get(membership);
        for (Member member : members) {
            member.update(stock, buyPrice, sellPrice);
        }
    }

}
