public class Bug3 {
    // Return true if the word reads the same forwards and backwards.
    static boolean isPalindrome(String word) {
        String reversed = "";
        for (int i = word.length() - 1; i >= 0; i--) {
            reversed += word.charAt(i);
        }
        return word == reversed;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("level")); // expected true
        System.out.println(isPalindrome("hello")); // expected false
        System.out.println(isPalindrome(""));      // expected true
    }
}
