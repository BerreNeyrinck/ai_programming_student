"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""


def insertion_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van insertion sort.

    Parameters:
        sequence (list): De lijst om te sorteren.

    Returns:
        list: De gesorteerde lijst.
    """
    if(len(sequence) > 1):
        for i in range(1, len(sequence)):
            value = sequence[i]
            j = i - 1

            while j >= 0 and value < sequence[j]:
                sequence[j + 1] = sequence[j]
                j -= 1
            sequence[j + 1] = value

    return sequence
        

def bubble_sort(sequence):

    if(len(sequence) > 1):
        for i in range(len(sequence)):
            swapped = False
            for j in range(0, len(sequence)-i-1):
                if sequence[j] > sequence[j+1]: #i?
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
                    swapped = True
            if(swapped == False):
                break

    return sequence




if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"INSERT Origineel: {origineel} -> Gesorteerd: {gesorteerd}")
    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = bubble_sort(lijst)
        print(f"BUBBLE Origineel: {origineel} -> Gesorteerd: {gesorteerd}")
        

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:
    # import random
    # import time
    # ...