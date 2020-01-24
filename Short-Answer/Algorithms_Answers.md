#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The `while` loop looks to be n^3, but the inner loop is increasing `a` by n^2 with each iteration. n^3 / n^2 = n, so the runtime is in O(n).


b) The `for` loop runs `n` times, and the inner `while` loop has `j` doubling with each iteration, which is log(n). The total runtime for this example is O(n log(n)).


c) `bunnyEars()` is called recursively once for every bunny. This runs in O(bunny) time.

## Exercise II

I am going to assume that a dropped egg increments f by one, whether or not it breaks.