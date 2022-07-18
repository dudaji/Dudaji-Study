public class Navigation{
    private RouteBehavior routeBehavior;

    public Navigation(RouteBehavior routeBehavior) {
        this.routeBehavior = routeBehavior;
    }

    public void buildRoute() {
        routeBehavior.buildRoute();
    }

    public void setBuildRoute(RouteBehavior routeBehavior) {
        this.routeBehavior = routeBehavior;
    }
}