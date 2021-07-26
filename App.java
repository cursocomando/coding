/*package App;*/

public class App {
    public static void main(String[] args) {
        SchoolGradingSystem sgs = new SchoolGradingSystem();
        sgs.readData(); //cuando lo hagamos, ya habría un n
        System.out.println(sgs.question1());
        System.out.println(sgs.question2());
        System.out.println(sgs.question3());
        System.out.println(sgs.question4());
    }
}
