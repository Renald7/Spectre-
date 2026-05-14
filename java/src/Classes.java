public class Classes {
    public static void main(String[] args) {
        
        System.out.println("╔═══════════════════════════════════╗");
        System.out.println("║     CLASSES IN JAVA (OOP)     ║");
        System.out.println("╚═══════════════════════════════════╝");
        System.out.println();
        
        // Create an object
        ProblemSolver solver = new ProblemSolver("Helper", 25);
        
        // Use the object
        System.out.println("Name: " + solver.name);
        System.out.println("Problems solved: " + solver.problemsSolved);
        
        // Call methods
        solver.solve("Database bug");
        solver.solve("API error");
        
        System.out.println("After solving 2 problems: " + solver.problemsSolved);
        
        // Create another object
        ProblemSolver solver2 = new ProblemSolver("World", 30);
        solver2.solve("Memory leak");
        
        System.out.println();
        System.out.println("Solver2 problems: " + solver2.problemsSolved);
    }
}

// ================== CLASS DEFINITION ==================
class ProblemSolver {
    // Properties (fields)
    String name;
    int age;
    int problemsSolved;
    
    // Constructor (special method)
    public ProblemSolver(String name, int age) {
        this.name = name;
        this.age = age;
        this.problemsSolved = 0;
        System.out.println("Created: " + name);
    }
    
    // Method
    public void solve(String problem) {
        problemsSolved++;
        System.out.println(name + " solved: " + problem);
    }
    
    // Method with return
    public String getStatus() {
        return name + " has solved " + problemsSolved + " problems!";
    }
}
