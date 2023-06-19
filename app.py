# Pass days (n) as argument
def solution(n):
    if n<4:
        probability = 2 ** (n - 1)
        number_of_ways_to_attend = 2 ** n
    else:
        previous_day_attended = 2
        previous_2_days_attended = 1
        previous_3_days_attended = 1
        P = 4
        count = 8
        for i in range(4,n+1):
            temp= previous_3_days_attended
            previous_3_days_attended = previous_2_days_attended
            previous_2_days_attended = previous_day_attended
            previous_day_attended = P
            P = count
            count = (count-temp) * 2 + temp
        
        probability = str(previous_3_days_attended + previous_2_days_attended + previous_day_attended)
        number_of_ways_to_attend = str(count)

    return probability+'/'+number_of_ways_to_attend



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
    n = 10
    result = solution(t["input"])
    if result == t["output"]:
        print(f"{t['name']} - PASSED")
    else:
        print(f"{t['name']} - FAILED")



