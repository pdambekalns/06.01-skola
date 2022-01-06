"""Uzrakstīt funkciju, kas dotajam nedēļas dienas numuram atgriež dienas nosaukumu vārdiem."""
import diena
dien=int(input("Ievadi dienas kārtas skaitli! "))
print("Diena pēc kārtas skaitļa sanāk", diena.kalendars(dien))