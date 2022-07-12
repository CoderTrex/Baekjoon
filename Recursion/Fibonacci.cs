using System;

class Fibonacci
{
    static void Main()
    {
        int num = int.Parse(Console.ReadLine());
        System.Console.WriteLine(fibo(num));
    }

    static int fibo(int n)
    {
        if (n <= 1)
            return n;
        else
            return fibo(n - 1) + fibo(n - 2);
    }
}