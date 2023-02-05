"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
                [
                    [21, 6, 25, 25, 17],
                    [14, 0, 6, 0, 2],
                    [1, 11, 16, 1, 17],
                    [11, 0, 16, 0, 5],
                    [26, 3, 14, 20, 6]
                ],
                ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']
            ],
            "answer": [
                ['h', 'e', 'l', 'l', 'o'],
                ['a', ' ', 'e', ' ', 'z'],
                ['b', 'i', 'm', 'b', 'o'],
                ['i', ' ', 'm', ' ', 'n'],
                ['t', 'r', 'a', 'c', 'e'],
            ],
        },
        {
            "input": [
                [
                    [19, 26, 8, 25, 18],
                    [24, 0, 24, 0, 8],
                    [4, 24, 23, 21, 3],
                    [3, 0, 26, 0, 13],
                    [8, 6, 15, 17, 13]
                ],
                ['world', 'rings', 'tache', 'water', 'racon', 'dress'],
            ],
            "answer": [
                ['w', 'o', 'r', 'l', 'd'],
                ['a', ' ', 'a', ' ', 'r'],
                ['t', 'a', 'c', 'h', 'e'],
                ['e', ' ', 'o', ' ', 's'],
                ['r', 'i', 'n', 'g', 's'],
            ],
        },
    ],
    "Extra": [
        {
            "input": [
                [
                    [19, 23, 22, 1, 23],
                    [8, 0, 9, 0, 6],
                    [10, 1, 6, 2, 22],
                    [13, 0, 8, 0, 18],
                    [22, 21, 18, 13, 22]
                ],
                ['users', 'crime', 'eagle', 'uncle', 'eking', 'siege']
            ],
            "answer": [
                ['u', 's', 'e', 'r', 's'],
                ['n', ' ', 'k', ' ', 'i'],
                ['c', 'r', 'i', 'm', 'e'],
                ['l', ' ', 'n', ' ', 'g'],
                ['e', 'a', 'g', 'l', 'e'],
            ],
        },
        {
            "input": [
                [
                    [14, 9, 24, 10, 14],
                    [24, 0, 13, 0, 13],
                    [13, 26, 13, 20, 18],
                    [6, 0, 25, 0, 9],
                    [14, 6, 9, 3, 14]
                ],
                ['sodas', 'loofa', 'slots', 'stars', 'ovoid', 'sales']
            ],
            "answer": [
                ['s', 'a', 'l', 'e', 's'],
                ['l', ' ', 'o', ' ', 'o'],
                ['o', 'v', 'o', 'i', 'd'],
                ['t', ' ', 'f', ' ', 'a'],
                ['s', 't', 'a', 'r', 's'],
            ],
        },
    ]
}
