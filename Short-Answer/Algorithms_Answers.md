#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The `while` loop looks to be n^3, but the inner loop is increasing `a` by n^2 with each iteration. n^3 / n^2 = n, so the runtime is in O(n).


b) The `for` loop runs `n` times, and the inner `while` loop has `j` doubling with each iteration, which is log(n). The total runtime for this example is O(n log(n)).


c) `bunnyEars()` is called recursively once for every bunny. This runs in O(bunny) time.

## Exercise II

A linear search to find floor f would be to start at the bottom and work up until finding a floor where the egg breaks. This, on average, will take about n/2 floors to check (assuming each building has a random floor where breakage starts).

A better approach to minimize the number of eggs dropped is to utilize a binary search approach.

At the beginning, all floors are viable options for floor f. Pick the middle floor as the first test-drop floor.

Drop an egg from the test-drop floor.

If it breaks, eliminate the curent floor and all floors above the test-drop floor from the viable list. Pick a new test-drop floor that is in the middle of the remaining viable floors.

If it does not break, eliminate all floors below the current floor from the viable list, but keep the current floor in the list. Pick a new test-drop floor that is in the middle of the remaining viable floors.

Repeat dropping eggs from the new test-drop floor until only one floor remains in the viable list. When that happens, the sole remaining floor is the highest floor from which one can safely drop an egg - floor f.

By halfing the number of remaining options each time, the worst-case number of eggs used is about log-base2(n-stories).
