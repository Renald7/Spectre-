public class Arrays {
    public static void main(String[] args) {
        
        System.out.println("╔═══════════════════════════════════╗");
        System.out.println("║        ARRAYS IN JAVA           ║");
        System.out.println("╚═══════════════════════════════════╝");
        System.out.println();
        
        // Array of integers
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        
        // Print array
        System.out.print("Numbers: ");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
        
        // Sum
        int sum = 0;
        for (int n : numbers) {
            sum += n;
        }
        System.out.println("Sum: " + sum);
        
        // String array
        System.out.println();
        String[] skills = {"Python", "Java", "Quantum", "ML", "Helping"};
        
        System.out.println("Skills:");
        for (String skill : skills) {
            System.out.println("  - " + skill);
        }
        
        // 2D Array (like matrix)
        System.out.println();
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        System.out.println("Matrix:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
