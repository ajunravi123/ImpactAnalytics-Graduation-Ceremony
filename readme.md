`Impact Analytics - Python Assignment - Ajun Ravi`

## Problem Statement

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

  The task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal


## Explanation of Solution-1 (/app.py)

1. The function takes an integer n as input, which represents the number of days.

2. It starts by checking if n is less than 4. If n is less than 4, it means the number of days is small enough to be handled separately, and the function returns the corresponding fraction 2**(n-1) / 2**n. The numerator 2**(n-1) represents the number of ways to attend classes over n days without missing four or more consecutive days, and the denominator 2**n represents the total number of possible attendance combinations over n days.

3. If n is 4 or greater, the function continues to the next part of the calculation.

4. Four variables are initialized:

- 'previous_day_attended' represents the number of ways to attend classes over n days with the previous day attended.
- 'previous_2_days_attended' represents the number of ways to attend classes over n days with the previous two days attended.
- 'previous_3_days_attended' represents the number of ways to attend classes over n days with the previous three days attended.
- P is initially set to 4 and represents the number of ways to attend classes over n days with the previous day missed but with the three previous days attended.
- count is initially set to 8 and represents the total count of ways to attend classes over n days.

5. The function enters a loop that iterates from 4 to n (inclusive) to calculate the number of ways to attend classes for each day.

6. Inside the loop, the values of 'previous_3_days_attended', 'previous_2_days_attended', 'previous_day_attended', P, and count are updated by shifting their values to the right. temp temporarily stores the previous value of 'previous_3_days_attended' to be used in the calculation.

7. The new values of 'previous_3_days_attended', 'previous_2_days_attended', and 'previous_day_attended' are updated accordingly, representing the number of ways to attend classes with the previous three days, previous two days, and the previous day attended, respectively.

8. P is updated to the previous value of count, representing the number of ways to attend classes with the previous day missed but with the three previous days attended.

9. count is updated based on the previous values of count and temp, representing the total count of ways to attend classes over n days.
- (count - temp) * 2 + temp calculates the number of new ways by doubling the difference between the current count and the previous value of 'previous_3_days_attended', and adding the previous value of 'previous_3_days_attended' itself.

10. After the loop finishes, the function returns a string representation of the solution:
-'previous_3_days_attended' + 'previous_2_days_attended' + 'previous_day_attended' represents the total number of ways to attend classes over n days, considering the previous three days, previous two days, and the previous day attended. count represents the total count of ways to attend classes over n days.


## Explanation of Solution-2 (/solution.py)

Solution-1 (app.py) is not completely my logic. I have taken help from internet for that logic. Because, that solution's Time & Space complexities was better than my logic.

My own solution is written in /solution.py file. So, please refer that for evaluation.

Time Complexity:

1. Generating Combinations: As mentioned earlier, generating all possible combinations of length n using itertools.product has a time complexity of O(2^n).

2. Iterating Over Combinations: The function iterates over each combination generated. Since there are 2^n combinations, the time complexity of this step is O(2^n).

3. Checking for 'AAAA': For each combination, the function checks if the string 'AAAA' is present. This check requires examining each character in the combination, which takes O(n) time.

Therefore, the overall time complexity of the print_combinations function is the sum of the time complexities of the above steps:

O(2^n) + O(2^n) + O(n) = O(2 * 2^n + n).


Space Complexity:

1. Combinations List: The function stores all the combinations in a list called combinations. The size of this list is 2^n since it contains all possible combinations. Therefore, the space complexity of storing the combinations is O(2^n).

2. Additional Variables: The function uses a few additional variables (ways_to_attend_classes, ways_to_absent_at_cermoney, etc.) to keep track of the counts. These variables do not depend on the input size and occupy constant space. Hence, their space complexity is O(1).

Thus, the overall space complexity of the print_combinations function is O(2^n).


#### Prerequisite
`Python` must be installed in your local machine.

#### How to run the code?
To run the code execute following command:
```
python solution.py
```
