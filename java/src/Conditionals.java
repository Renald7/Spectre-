public class Conditionals {
    public static void main(String[] args) {
        
        System.out.println("╔═══════════════════════════════════╗");
        System.out.println("║   IF/ELSE IN JAVA             ║");
        System.out.println("╚═══════════════════════════════════╝");
        System.out.println();
        
        int age = 18;
        
        // Simple if
        if (age >= 18) {
            System.out.println("✓ You are an adult!");
        }
        
        // If-else
        int score = 75;
        System.out.println();
        System.out.println("Score: " + score);
        
        if (score >= 90) {
            System.out.println("Grade: A");
        } else if (score >= 80) {
            System.out.println("Grade: B");
        } else if (score >= 70) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }
        
        // Switch (like match in Python)
        System.out.println();
        int day = 3;
        String dayName;
        
        switch (day) {
            case 1: dayName = "Monday"; break;
            case 2: dayName = "Tuesday"; break;
            case 3: dayName = "Wednesday"; break;
            case 4: dayName = "Thursday"; break;
            case 5: dayName = "Friday"; break;
            case 6: dayName = "Saturday"; break;
            case 7: dayName = "Sunday"; break;
            default: dayName = "Invalid"; break;
        }
        System.out.println("Day " + day + " is " + dayName);
    }
}
