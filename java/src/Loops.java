public class Loops {
    public static void main(String[] args) {
        
        System.out.println("╔═══════════════════════════════════╗");
        System.out.println("║        LOOPS IN JAVA          ║");
        System.out.println("╚═══════════════════════════════════╝");
        System.out.println();
        
        // For loop
        System.out.println("For Loop (1-5):");
        for (int i = 1; i <= 5; i++) {
            System.out.println("  Count: " + i);
        }
        
        // While loop
        System.out.println();
        System.out.println("While Loop:");
        int count = 1;
        while (count <= 3) {
            System.out.println("  Count is: " + count);
            count++;
        }
        
        // Do-while (runs at least once)
        System.out.println();
        System.out.println("Do-While Loop:");
        int x = 5;
        do {
            System.out.println("  x = " + x);
            x--;
        } while (x > 0);
        
        // Nested loop (multiplication table)
        System.out.println();
        System.out.println("Multiplication Table (1-3):");
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.print(i + "x" + j + "=" + (i*j) + "  ");
            }
            System.out.println();
        }
    }
}
