public class Factorial {

	public static void main (String[] args) {
		int number = 4;
		int factorial = 1;
		while (number > 1) {
			factorial *= number;
			number--;
		}
		System.out.println("Factorial of 4 is = " + factorial);
	}
}
