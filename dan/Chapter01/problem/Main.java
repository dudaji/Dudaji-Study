public class Main {
    public static void main(String[] args) {
        Navigation navigation = new Navigation(new Car());
        navigation.buildRoute("강남역", "양재역");
        navigation.setBuildRoute(new PublicTransport());
    }
}