from functools import lru_cache


def longest_common_subsequence_length(alice, bob):
    n, m = len(alice), len(bob)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill the DP table with LCS lengths
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if alice[i - 1] == bob[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


@lru_cache(None)
def collect_all_lcs(dp, alice, bob, i, j, lcs_length, current_path):
    if lcs_length == 0:
        return {current_path}
    if i == 0 or j == 0:
        return set()

    result = set()
    if alice[i - 1] == bob[j - 1]:
        result.update(collect_all_lcs(dp, alice, bob, i - 1, j - 1, lcs_length - 1, alice[i - 1] + current_path))
    else:
        if dp[i - 1][j] == dp[i][j]:
            result.update(collect_all_lcs(dp, alice, bob, i - 1, j, lcs_length, current_path))
        if dp[i][j - 1] == dp[i][j]:
            result.update(collect_all_lcs(dp, alice, bob, i, j - 1, lcs_length, current_path))

    return result


def trip_dynamic_programming(test_cases):
    results = []
    for alice, bob in test_cases:
        # Step 1: Build DP table
        dp = longest_common_subsequence_length(alice, bob)
        lcs_length = dp[len(alice)][len(bob)]

        # Step 2: Collect all longest common subsequences
        # Convert dp to tuple of tuples for memoization
        dp_tuple = tuple(tuple(row) for row in dp)
        all_lcs = collect_all_lcs(dp_tuple, alice, bob, len(alice), len(bob), lcs_length, "")

        # Step 3: Sort and append to results, limit to 1000 results
        sorted_lcs = sorted(all_lcs)[:1000]
        results.append(sorted_lcs)

    return results


# Input
t = int(input())
test_cases = [(input().strip(), input().strip()) for _ in range(t)]
results = trip_dynamic_programming(test_cases)

# Output
for i, result in enumerate(results):
    for trip in result:
        print(trip)
    if i < len(results) - 1:
        print()
