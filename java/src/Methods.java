public class Methods {
    
    // Main method - entry point
    public static void main(String[] args) {
        
        System.out.println("╔═══════════════════════════════════╗");
        System.out.println("║     METHODS IN JAVA           ║");
        System.out.println("╚═══════════════════════════════════╝");
        System.out.println();
        
        // Call methods
        greet("Friend");
        greet("World");
        
        // Method with return
        int result = add(5, 3);
        System.out.println("5 + 3 = " + result);
        
        // Method with multiple parameters
        printMessage("Hello", 3);
        
        // Recursion example
        int factorial = factorial(5);
        System.out.println("5! = " + factorial);
    }
    
    // Simple method (no return)
    public static void greet(String name) {
        System.out.println("Hello " + name + "!");
    }
    
    // Method with return value
    public static int add(int a, int b) {
        return a + b;
    }
    
    // Method with multiple parameters
    public static void printMessage(String msg, int times) {
        System.out.println("Printing " + msg + " " + times + " times:");
        for (int i = 0; i < times; i++) {
            System.out.println("  " + msg);
        }
    }
    
    // Recursive method
    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
