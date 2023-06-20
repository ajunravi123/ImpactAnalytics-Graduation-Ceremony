import itertools

def solution(n):
    characters = ['A', 'P'] # A for Absent and P for Present
    ways_to_attend_classes = 0
    ways_to_absent_at_cermoney = 0
    combinations = [''.join(combination) for combination in itertools.product(characters, repeat=n)]
    for combination in combinations:
        if 'AAAA' not in combination:
            ways_to_attend_classes += 1
            if combination[-1] == "A":
                ways_to_absent_at_cermoney += 1

    return f"{ways_to_absent_at_cermoney}/{ways_to_attend_classes}"


# Add all test cases here
test_cases = [
    {
        "name": "Test Case 1",
        "input" : 5,
        "output" : "14/29"
    },
    {
        "name": "Test Case 2",
        "input" : 10,
        "output" : "372/773"
    }
]

# Validating test cases
print("Running Test-Cases")
for t in test_cases:
    result = solution(t["input"])
    if result == t["output"]:
        print(f"{t['name']} - PASSED")
    else:
        print(f"{t['name']} - FAILED")