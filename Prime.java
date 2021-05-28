import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Prime {

	private static boolean isPrime(int num) {
		// Return true if the number is prime
		if (num < 2) {
			return false;
		}
		for (int i = 2; i < num; i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}

	private static void primesLessThan(int num) {
		// Print a list of all primes less than num.
		List<Integer> primes = new ArrayList<>();
		for (int i = 2; i < num; i++) {
			if (isPrime(i)) primes.add(i);
		}
		System.out.println(Arrays.toString(primes.toArray()));
	}

	public static void main(String [] args) {
		primesLessThan(50);
	}
}
