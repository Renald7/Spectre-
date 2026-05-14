package faang;

/**
 * ╔═══════════════════════════════════════════════════════════════════════════════╗
 * ║                  🚀 FAANG MASTER - ALL LEVELS 🚀                      ║
 * ╚═══════════════════════════════════════════════════════════════════════════════╝
 */
public class FAANGMaster {
    public static void main(String[] args) {
        printBanner();
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 1: ARRAYS & STRINGS
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║           LESSON 1: ARRAYS & STRINGS                      ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // Example 1: Two Pointers
        System.out.println("▶ Example 1: Two Pointers - Reverse Array");
        int[] arr = {1, 2, 3, 4, 5};
        System.out.print("Original: ");
        printArray(arr);
        
        reverse(arr);
        System.out.print("Reversed: ");
        printArray(arr);
        
        // Example 2: Sliding Window
        System.out.println("\n▶ Example 2: Maximum Sum Subarray (Kadane's)");
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int maxSum = maxSubArray(nums);
        System.out.println("Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]");
        System.out.println("Maximum Sum: " + maxSum);
        
        // Example 3: String manipulation
        System.out.println("\n▶ Example 3: Reverse String");
        String s = "Hello World";
        System.out.println("Original: " + s);
        System.out.println("Reversed: " + reverseString(s));
        
        // Example 4: Palindrome
        System.out.println("\n▶ Example 4: Palindrome Check");
        String palindrome = "racecar";
        System.out.println("'" + palindrome + "' is palindrome: " + isPalindrome(palindrome));
        
        // Example 5: Anagram
        System.out.println("\n▶ Example 5: Anagram Check");
        String s1 = "listen";
        String s2 = "silent";
        System.out.println("'" + s1 + "' and '" + s2 + "' are anagrams: " + isAnagram(s1, s2));
        
        // Example 6: Maximum Subarray Length K
        System.out.println("\n▶ Example 6: Maximum Average Subarray");
        int[] nums2 = {1,12,-5,-6,50,3};
        int k = 4;
        System.out.println("Array: [1,12,-5,-6,50,3], K=" + k);
        System.out.println("Max Average: " + maxAverage(nums2, k));
        
        // Example 7: Merge Sorted Arrays
        System.out.println("\n▶ Example 7: Merge Two Sorted Arrays");
        int[] a1 = {1, 3, 5, 7};
        int[] a2 = {2, 4, 6, 8};
        int[] merged = mergeSortedArrays(a1, a2);
        System.out.print("Merged: ");
        printArray(merged);
        
        // Example 8: Remove Duplicates
        System.out.println("\n▶ Example 8: Remove Duplicates (In Place)");
        int[] withDupes = {1, 1, 2, 2, 2, 3, 4, 4, 5};
        System.out.print("Original: ");
        printArray(withDupes);
        int newLen = removeDuplicates(withDupes);
        System.out.println("New length: " + newLen);
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 2: LINKED LISTS
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║           LESSON 2: LINKED LISTS                          ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // Create linked list
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        
        System.out.println("▶ Example 1: Reverse Linked List");
        System.out.print("Original: ");
        printList(head);
        ListNode reversed = reverseList(head);
        System.out.print("Reversed: ");
        printList(reversed);
        
        // Detect cycle
        System.out.println("\n▶ Example 2: Detect Cycle");
        ListNode head2 = new ListNode(1);
        head2.next = new ListNode(2);
        head2.next.next = new ListNode(3);
        head2.next.next.next = head2.next; // Creates cycle
        System.out.println("Has cycle: " + hasCycle(head2));
        
        // Merge two sorted lists
        System.out.println("\n▶ Example 3: Merge Two Sorted Lists");
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(3);
        l1.next.next = new ListNode(5);
        
        ListNode l2 = new ListNode(2);
        l2.next = new ListNode(4);
        l2.next.next = new ListNode(6);
        
        System.out.print("List 1: ");
        printList(l1);
        System.out.print("List 2: ");
        printList(l2);
        
        ListNode merged = mergeTwoLists(l1, l2);
        System.out.print("Merged: ");
        printList(merged);
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 3: STACKS & QUEUES
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║           LESSON 3: STACKS & QUEUES                       ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // Valid Parentheses
        System.out.println("▶ Example 1: Valid Parentheses");
        String brackets = "{[()]}";
        System.out.println("'" + brackets + "' is valid: " + isValid(brackets));
        
        // Min Stack
        System.out.println("\n▶ Example 2: Min Stack");
        MinStack minStack = new MinStack();
        minStack.push(5);
        minStack.push(2);
        minStack.push(8);
        System.out.println("Push: 5, 2, 8");
        System.out.println("Min: " + minStack.getMin());
        System.out.println("Pop: " + minStack.pop());
        System.out.println("Min after pop: " + minStack.getMin());
        
        // Implement Queue using Stacks
        System.out.println("\n▶ Example 3: Queue using Stacks");
        MyQueue queue = new MyQueue();
        queue.push(1);
        queue.push(2);
        queue.push(3);
        System.out.println("Push: 1, 2, 3");
        System.out.println("Pop: " + queue.pop());
        System.out.println("Peek: " + queue.peek());
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 4: TREES
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║                    LESSON 4: TREES                          ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // Build a tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        
        System.out.println("▶ Example 1: Binary Tree Traversal");
        System.out.print("Inorder: ");
        inorderTraversal(root);
        System.out.println();
        System.out.print("Preorder: ");
        preorderTraversal(root);
        System.out.println();
        System.out.print("Postorder: ");
        postorderTraversal(root);
        System.out.println();
        
        // Max Depth
        System.out.println("\n▶ Example 2: Maximum Depth");
        System.out.println("Max depth: " + maxDepth(root));
        
        // Validate BST
        System.out.println("\n▶ Example 3: Validate BST");
        System.out.println("Is valid BST: " + isValidBST(root));
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 5: GRAPHS
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║                    LESSON 5: GRAPHS                         ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // BFS
        System.out.println("▶ Example 1: Breadth-First Search (BFS)");
        int[][] graph = {{}, {2,3,4}, {1}, {1,5}, {2,6}, {3}, {4}};
        System.out.print("BFS from node 1: ");
        bfs(graph, 1);
        
        // DFS
        System.out.println("\n▶ Example 2: Depth-First Search (DFS)");
        System.out.print("DFS from node 1: ");
        dfs(graph, 1, new boolean[7], new StringBuilder());
        
        // Number of Islands
        System.out.println("\n▶ Example 3: Number of Islands");
        char[][] grid = {
            {'1','1','1','1','0'},
            {'1','1','0','1','0'},
            {'1','0','0','0','0'},
            {'0','0','0','0','0'}
        };
        System.out.println("Grid has " + numIslands(grid) + " islands");
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 6: DYNAMIC PROGRAMMING
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║           LESSON 6: DYNAMIC PROGRAMMING                     ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // Fibonacci
        System.out.println("▶ Example 1: Fibonacci");
        System.out.print("Fibonacci(10): ");
        for (int i = 0; i <= 10; i++) {
            System.out.print(fib(i) + " ");
        }
        
        // Climbing Stairs
        System.out.println("\n\n▶ Example 2: Climbing Stairs");
        System.out.println("Ways to climb 5 stairs: " + climbStairs(5));
        
        // Coin Change
        System.out.println("\n▶ Example 3: Coin Change");
        int[] coins = {1, 2, 5};
        System.out.println("Coins: [1,2,5], Target: 11");
        System.out.println("Minimum coins: " + coinChange(coins, 11));
        
        // Longest Increasing Subsequence
        System.out.println("\n▶ Example 4: Longest Increasing Subsequence");
        int[] lis = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println("Array: [10,9,2,5,3,7,101,18]");
        System.out.println("LIS length: " + lengthOfLIS(lis));
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 7: SORTING & SEARCHING
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║        LESSON 7: SORTING & SEARCHING                       ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // Merge Sort
        System.out.println("▶ Example 1: Merge Sort");
        int[] toSort = {64, 34, 25, 12, 22, 11, 90};
        System.out.print("Original: ");
        printArray(toSort);
        mergeSort(toSort, 0, toSort.length - 1);
        System.out.print("Sorted: ");
        printArray(toSort);
        
        // Binary Search
        System.out.println("\n▶ Example 2: Binary Search");
        int[] sorted = {1, 3, 5, 7, 9, 11, 13, 15};
        System.out.print("Array: ");
        printArray(sorted);
        System.out.println("Search 7: index " + binarySearch(sorted, 7));
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 8: RECURSION & BACKTRACKING
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║        LESSON 8: RECURSION & BACKTRACKING                   ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        // N-Queens
        System.out.println("▶ Example 1: N-Queens (4-Queens)");
        solveNQueens(4);
        
        // Permutations
        System.out.println("\n▶ Example 2: Permutations");
        int[] perm = {1, 2, 3};
        System.out.print("Permutations of [1,2,3]: ");
        permute(perm, 0);
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 9: SYSTEM DESIGN BASICS
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║              LESSON 9: SYSTEM DESIGN                         ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        System.out.println("▶ System Design Patterns:\n");
        
        System.out.println("1. SCALABILITY:");
        System.out.println("   - Horizontal Scaling: Add more machines");
        System.out.println("   - Vertical Scaling: Add more resources to machine");
        System.out.println("   - Caching: Redis, Memcached");
        System.out.println("   - Load Balancing: Round Robin, Least Connections");
        
        System.out.println("\n2. DATABASE PATTERNS:");
        System.out.println("   - SQL: ACID, PostgreSQL, MySQL");
        System.out.println("   - NoSQL: CAP Theorem, MongoDB, Cassandra");
        System.out.println("   - Sharding: Horizontal partitioning");
        System.out.println("   - Replication: Master-Slave, Multi-Master");
        
        System.out.println("\n3. MICROSERVICES:");
        System.out.println("   - API Gateway: Single entry point");
        System.out.println("   - Service Discovery: Consul, Eureka");
        System.out.println("   - Circuit Breaker: Resilience");
        System.out.println("   - Message Queues: Kafka, RabbitMQ");
        
        System.out.println("\n4. DESIGN QUESTIONS TO PRACTICE:");
        System.out.println("   - Design URL Shortener (bit.ly)");
        System.out.println("   - Design Twitter Timeline");
        System.out.println("   - Design YouTube");
        System.out.println("   - Design Uber");
        System.out.println("   - Design WhatsApp");
        
        // ═══════════════════════════════════════════════════════════════════════
        // LESSON 10: PRODUCTION CODE
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n╔═══════════════════════════════════════════════════════════════════╗");
        System.out.println("║           LESSON 10: PRODUCTION CODE                         ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════╝\n");
        
        System.out.println("▶ Production Best Practices:\n");
        
        System.out.println("1. ERROR HANDLING:");
        System.out.println("   - Always use try-catch");
        System.out.println("   - Never swallow exceptions");
        System.out.println("   - Log meaningful errors");
        
        System.out.println("\n2. CODE REVIEW CHECKLIST:");
        System.out.println("   - Time complexity: O(n)? O(log n)?");
        System.out.println("   - Space complexity: O(n)? O(1)?");
        System.out.println("   - Edge cases: null, empty, negative");
        System.out.println("   - Variable names: descriptive");
        
        System.out.println("\n3. TESTING:");
        System.out.println("   - Unit tests: Test smallest units");
        System.out.println("   - Integration tests: Test components");
        System.out.println("   - E2E tests: Test full flow");
        
        System.out.println("\n4. CI/CD:");
        System.out.println("   - Git hooks");
        System.out.println("   - Automated tests");
        System.out.println("   - Code linting");
        System.out.println("   - Deployment automation");
        
        // ═══════════════════════════════════════════════════════════════════════
        // FINISH
        // ═══════════════════════════════════════════════════════════════════════
        System.out.println("\n\n");
        System.out.println("╔═══════════════════════════════════════════════════════════════════════╗");
        System.out.println("║                                                                       ║");
        System.out.println("║              🎓  FAANG MASTER - COMPLETE!  🎓                   ║");
        System.out.println("║                                                                       ║");
        System.out.println("║              Now Go Solve 500+ Problems!                          ║");
        System.out.println("║                                                                       ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════╝");
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // ARRAY & STRING METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static void reverse(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
    
    static int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }
    
    static String reverseString(String s) {
        return new StringBuilder(s).reverse().toString();
    }
    
    static boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }
    
    static boolean isAnagram(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int[] count = new int[256];
        for (int i = 0; i < s1.length(); i++) {
            count[s1.charAt(i)]++;
            count[s2.charAt(i)]--;
        }
        for (int c : count) if (c != 0) return false;
        return true;
    }
    
    static double maxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        double maxSum = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum / k;
    }
    
    static int[] mergeSortedArrays(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        while (i < a.length && j < b.length) {
            if (a[i] < b[j]) result[k++] = a[i++];
            else result[k++] = b[j++];
        }
        while (i < a.length) result[k++] = a[i++];
        while (j < b.length) result[k++] = b[j++];
        return result;
    }
    
    static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int slow = 0;
        for (int fast = 1; fast < nums.length; fast++) {
            if (nums[fast] != nums[slow]) {
                slow++;
                nums[slow] = nums[fast];
            }
        }
        return slow + 1;
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // LINKED LIST METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    
    static boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
    
    static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        if (l1 != null) curr.next = l1;
        if (l2 != null) curr.next = l2;
        return dummy.next;
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // STACK & QUEUE METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static boolean isValid(String s) {
        java.util.Stack<Character> stack = new java.util.Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '{') stack.push('}');
            else if (c == '[') stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }
        return stack.isEmpty();
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // TREE METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static void inorderTraversal(TreeNode root) {
        if (root == null) return;
        inorderTraversal(root.left);
        System.out.print(root.val + " ");
        inorderTraversal(root.right);
    }
    
    static void preorderTraversal(TreeNode root) {
        if (root == null) return;
        System.out.print(root.val + " ");
        preorderTraversal(root.left);
        preorderTraversal(root.right);
    }
    
    static void postorderTraversal(TreeNode root) {
        if (root == null) return;
        postorderTraversal(root.left);
        postorderTraversal(root.right);
        System.out.print(root.val + " ");
    }
    
    static int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
    
    static boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    static boolean isValidBST(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return isValidBST(node.left, min, node.val) && isValidBST(node.right, node.val, max);
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // GRAPH METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static void bfs(int[][] graph, int start) {
        java.util.Queue<Integer> queue = new java.util.LinkedList<>();
        boolean[] visited = new boolean[graph.length];
        queue.add(start);
        visited[start] = true;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
    }
    
    static void dfs(int[][] graph, int node, boolean[] visited, StringBuilder sb) {
        visited[node] = true;
        sb.append(node).append(" ");
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(graph, neighbor, visited, sb);
            }
        }
        System.out.print(sb.toString());
    }
    
    static int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfsIslands(grid, i, j);
                }
            }
        }
        return count;
    }
    
    static void dfsIslands(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == '0') return;
        grid[i][j] = '0';
        dfsIslands(grid, i+1, j);
        dfsIslands(grid, i-1, j);
        dfsIslands(grid, i, j+1);
        dfsIslands(grid, i, j-1);
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // DP METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static int fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
    
    static int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
    
    static int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        java.util.Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
    
    static int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;
        for (int num : nums) {
            int i = java.util.Arrays.binarySearch(dp, 0, len, num);
            if (i < 0) i = -(i + 1);
            dp[i] = num;
            if (i == len) len++;
        }
        return len;
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // SORTING & SEARCHING
    // ═══════════════════════════════════════════════════════════════════════
    
    static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }
    
    static void merge(int[] arr, int left, int mid, int right) {
        int[] leftArr = java.util.Arrays.copyOfRange(arr, left, mid + 1);
        int[] rightArr = java.util.Arrays.copyOfRange(arr, mid + 1, right + 1);
        int i = 0, j = 0, k = left;
        while (i < leftArr.length && j < rightArr.length) {
            if (leftArr[i] <= rightArr[j]) arr[k++] = leftArr[i++];
            else arr[k++] = rightArr[j++];
        }
        while (i < leftArr.length) arr[k++] = leftArr[i++];
        while (j < rightArr.length) arr[k++] = rightArr[j++];
    }
    
    static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // BACKTRACKING
    // ═══════════════════════════════════════════════════════════════════════
    
    static void solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] row : board) java.util.Arrays.fill(row, '.');
        solveNQueens(board, 0);
    }
    
    static void solveNQueens(char[][] board, int row) {
        if (row == board.length) {
            System.out.println("Solution:");
            for (char[] row2 : board) {
                System.out.println(new String(row2));
            }
            System.out.println();
            return;
        }
        for (int col = 0; col < board.length; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                solveNQueens(board, row + 1);
                board[row][col] = '.';
            }
        }
    }
    
    static boolean isSafe(char[][] board, int row, int col) {
        for (int i = 0; i < row; i++) if (board[i][col] == 'Q') return false;
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) if (board[i][j] == 'Q') return false;
        for (int i = row, j = col; i >= 0 && j < board.length; i--, j++) if (board[i][j] == 'Q') return false;
        return true;
    }
    
    static void permute(int[] nums, int start) {
        if (start == nums.length) {
            System.out.print(java.util.Arrays.toString(nums) + " ");
            return;
        }
        for (int i = start; i < nums.length; i++) {
            int temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;
            permute(nums, start + 1);
            temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;
        }
    }
    
    // ═══════════════════════════════════════════════════════════════════════
    // HELPER METHODS
    // ═══════════════════════════════════════════════════════════════════════
    
    static void printArray(int[] arr) {
        for (int n : arr) System.out.print(n + " ");
        System.out.println();
    }
    
    static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " -> ");
            head = head.next;
        }
        System.out.println("null");
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// DATA STRUCTURES
// ═══════════════════════════════════════════════════════════════════════════════

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

class MinStack {
    java.util.Stack<Integer> stack = new java.util.Stack<>();
    java.util.Stack<Integer> minStack = new java.util.Stack<>();
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) minStack.push(val);
    }
    
    public int pop() {
        if (!minStack.isEmpty() && stack.peek().equals(minStack.peek())) minStack.pop();
        return stack.pop();
    }
    
    public int top() { return stack.peek(); }
    public int getMin() { return minStack.peek(); }
}

class MyQueue {
    java.util.Stack<Integer> in = new java.util.Stack<>();
    java.util.Stack<Integer> out = java.util.Stack<>();
    
    public void push(int x) { in.push(x); }
    public int pop() {
        if (out.isEmpty()) while (!in.isEmpty()) out.push(in.pop());
        return out.pop();
    }
    public int peek() {
        if (out.isEmpty()) while (!in.isEmpty()) out.push(in.pop());
        return out.peek();
    }
    public boolean empty() { return in.isEmpty() && out.isEmpty(); }
}
