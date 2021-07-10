class PalindromicNumbers {
	public static void main(String[] args) {
		int n = 454;
		int original = n;
		int reverse = 0;
		while (n > 0) {
			int digit = n % 10;
			reverse = (reverse * 10) + digit;
			n = n /10;
		}
		System.out.println(original == reverse ? "Palindrome number":"Not palindrome number");
	}
}

