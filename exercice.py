#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for letter in prefixes:
        names.append(letter + suffixe)
    return names


def prime_integer_summation() -> int:
    primes = []
    is_prime = True
    for number in range(2, 100):
        is_prime = True
        for divider in range(2, number):
            if number % divider == 0:
                is_prime = False
        if is_prime:
            primes.append(number)

    sum = 0
    for number in primes:
        sum += number
    return sum


def factorial(number: int) -> int:
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


def use_continue() -> None:
    nombres = []
    for number in range(1, 11):
        if number == 5:
            continue
        else:
            nombres.append(number)
    print(nombres)
    return None


def verify_ages(groups: List[List[int]]) -> List[bool]:
    groupes_acceptables = []
    older_70, equals_50, younger_18, equals_25 = False, False, False, False

    for group in groups:
        if len(group) > 3 and len(group) < 11:
            older_70, equals_50, younger_18, equals_25 = False, False, False, False
            for age in group:
                if age == 25:
                    equals_25 = True
                if age < 18:
                    younger_18 = True
                if age == 50:
                    equals_50 = True
                if age > 70:
                    older_70 = True          
            if equals_25:
                groupes_acceptables.append(group)
            else:
                if younger_18 == False and equals_50 == False and older_70 == False:
                    groupes_acceptables.append(group)
                elif younger_18 == False and equals_50 == False and older_70:
                    groupes_acceptables.append(group)
                elif younger_18 == False and equals_50 and older_70 == False:
                    groupes_acceptables.append(group)
                else:
                    continue     
    return groupes_acceptables


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
