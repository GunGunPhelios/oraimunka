using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace Oramunka
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* string kerdes1 = "Mi Magyarország fővárosa?";
             string valasz1 = "Budapest";
             string kerdes2 = "Hány napból áll egy év, ha nem szökőév.";
             int valasz2 = 365;

             int talalat = 0;
             do
             {
                 Console.WriteLine(kerdes1);
                 string Felhasznalovalasz = Console.ReadLine();
                 talalat++;

                 if (Felhasznalovalasz == valasz1)
                 {
                     Console.WriteLine($"Eltaláltad, a helyes válasz: {valasz1}");
                     Console.WriteLine($"Találgatások száma: {talalat}");
                     break;
                 }
                 else
                 {
                     Console.WriteLine("Nem helyes a válasz!");

                 }
                 while (true) ;

                 do {
                     Console.WriteLine(kerdes2);
                     int userValasz = int.Parse(Console.ReadLine(());
                     talalat++;

                     if (userValasz == valasz2) ;
                     {
                         Console.WriteLine($"Helyes válasz {valasz2} volt");
                         Console.WriteLine($"Találgatások száma: {talalat)"});
                     break;

                 }
                 else
                 {
                     Console.WriteLine("Nem ez volt a helyes válasz.") /*
            */
            /*
        while (true);
        Random random= new Random();
        int randomszam = random.Next(1, 20);

        do
        {
            Console.WriteLine("Gondoltam egy számra 1-20 között:");
            int bekertszam=int.Parse(Console.ReadLine());
            if (bekertszam == randomszam)
            {
                Console.WriteLine($"$Eltaláltad a {randomszam}ra gondoltam. ");
            }
        }
        else
        {
           Console.WriteLine("Nem talált, Próbáld újra!");

        }



        Console.ReadKey();
            */
            
            
                Console.WriteLine("Üdvözöllek a Kő, Papír, Olló játékban!");
                Console.WriteLine("Írd be a választásodat: Kő, Papír vagy Olló (vagy írd be: Kilépés a játék befejezéséhez).");

                string[] lehetosegek = { "kő", "papír", "olló" };
                Random random = new Random();

                while (true)
                {
                    // A játékos választása
                    Console.Write("\nA te választásod: ");
                    string jatekosValasztas = Console.ReadLine().ToLower();

                    // Kilépés ellenőrzése
                    if (jatekosValasztas == "kilépés")
                    {
                        Console.WriteLine("Köszönöm, hogy játszottál! Viszlát!");
                        break;
                    }

                    // Ellenőrzés, hogy érvényes-e a választás
                    if (!Array.Exists(lehetosegek, elem => elem == jatekosValasztas))
                    {
                        Console.WriteLine("Érvénytelen választás, próbáld újra: Kő, Papír vagy Olló.");
                        continue;
                    }

                    // A számítógép választása
                    string gepValasztas = lehetosegek[random.Next(lehetosegek.Length)];
                    Console.WriteLine($"A gép választása: {gepValasztas}");

                    // Eredmény meghatározása
                    if (jatekosValasztas == gepValasztas)
                    {
                        Console.WriteLine("Döntetlen!");
                    }
                    else if ((jatekosValasztas == "kő" && gepValasztas == "olló") ||
                             (jatekosValasztas == "papír" && gepValasztas == "kő") ||
                             (jatekosValasztas == "olló" && gepValasztas == "papír"))
                    {
                        Console.WriteLine("Nyertél!");
                    }
                    else
                    {
                        Console.WriteLine("Vesztettél!");
                    }
                }
            }
        }
    };

