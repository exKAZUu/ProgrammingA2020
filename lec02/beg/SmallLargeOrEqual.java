package lec02;

import java.util.Scanner;

public class SmallLargeOrEqual {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        sc.close();
        if (a < b)
            System.out.println("a < b");
        else if (a == b)
            System.out.println("a == b");
        else
            System.out.println("a > b");
    }
}