public class Car implements RouteStrategy {
    @Override
    public void buildRoute(String startingPoint, String destination) {
        System.out.println("buildroute by car");
    }
    
}
