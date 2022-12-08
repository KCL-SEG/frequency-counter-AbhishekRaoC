"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        stringed = str(i)
        if stringed not in frequencies.keys():
            frequencies[stringed] = 1
        else:
            val = frequencies.get(stringed) + 1
            frequencies.update({stringed : val})

    return frequencies
