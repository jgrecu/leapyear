public class LeapYear {

    public static void main(String[] args) {
        System.out.println(isLeapYear(2020));
    }

    public static boolean isLeapYear(int year) {
        if (year % 4 == 0) {
            if (year % 400 == 0) {
                return true;
            } else if (year % 100 == 0) {
                return false;
            }
            return true;
        }
        return false;
    }
}
