# JAVA QUICK REFERENCE

## Basic Structure
```java
public class MyClass {
    public static void main(String[] args) {
        // code here
    }
}
```

## Variables
```java
String name = "John";
int age = 25;
double price = 19.99;
boolean isTrue = true;
```

## Arrays
```java
int[] numbers = {1, 2, 3, 4, 5};
String[] names = {"A", "B", "C"};
int[][] matrix = {{1,2}, {3,4}};
```

## Loops
```java
// For
for (int i = 0; i < 10; i++) { }

// For-each
for (int n : numbers) { }

// While
while (condition) { }

// Do-while
do { } while (condition);
```

## Conditionals
```java
if (condition) { } 
else if (condition) { } 
else { }

switch(variable) {
    case 1: break;
    default: break;
}
```

## Methods
```java
public static int add(int a, int b) {
    return a + b;
}
```

## Classes
```java
class Person {
    String name;
    int age;
    
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    void speak() {
        System.out.println("Hello!");
    }
}
```

## Key Differences: Python vs Java

| Python | Java |
|--------|------|
| `def` | `public static` |
| `print()` | `System.out.println()` |
| `list` | `ArrayList` or `[]` |
| `True/False` | `true/false` |
| `if x:` | `if (x != 0) { }` |
| `None` | `null` |
| `def greet(name):` | `public void greet(String name)` |
