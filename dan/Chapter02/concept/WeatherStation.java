public class WeatherStation {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        CurrentConditionsDisplay currentDisplay =
        new CurrentConditionsDisplay(weatherData);

        HumidityDisplay currentDisplay2 = new HumidityDisplay(weatherData);

        weatherData.setMeasurements(80, 65, 30.4f);
        weatherData.setMeasurements(49, 43, 22.7f);
        weatherData.setMeasurements(69, 54, 38.1f);
    }
}
