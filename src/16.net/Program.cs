using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System;
using System.Collections.Generic;

namespace _16.net
{
    class Program
    {
        static void Main(string[] args)
        {
            var inp = "12345678";
            // inp = inp.Repeat(10000);

            for (var i = 0; i < 100; i++)
            {
                Console.WriteLine(inp);
                inp = dofft(inp);
            }

            // var offset = int.Parse(inp.Substring(0, 7));
            Console.WriteLine(inp.Substring(0, 8));
        }

        static string dofft(string numbers)
        {
            var output = "";
            for (var i = 0; i < numbers.Length; i++)
            {
                var pc = Cycle(GetPattern(i + 1));
                var enumerator = pc.GetEnumerator();

                enumerator.MoveNext();
                enumerator.MoveNext();

                var digit = 0;
                foreach (var n in numbers)
                {
                    digit += int.Parse(n.ToString()) * enumerator.Current;
                    enumerator.MoveNext();
                }

                output = output + (Math.Abs(digit) % 10).ToString();
            }

            return output;
        }

        static IEnumerable<int> Cycle(IEnumerable<int> pattern)
        {
            while (true)
            {
                foreach (var i in pattern)
                {
                    yield return i;
                }
            }
        }

        static IEnumerable<int> GetPattern(int ind)
        {
            for (var i = 0; i < ind; i++) yield return 0;
            for (var i = 0; i < ind; i++) yield return 1;
            for (var i = 0; i < ind; i++) yield return 0;
            for (var i = 0; i < ind; i++) yield return -1;
        }
    }

    public static class StringExtension
    {
        public static string Repeat(this string text, int count)
        {
            return String.Concat(Enumerable.Repeat(text, count));
        }
    }
}
