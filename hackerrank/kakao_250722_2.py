def longestChain(words):
    words.sort(key=len)
    dp = {}
    max_chain = 0
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_chain = max(max_chain, dp[word])
    
    return max_chain

if __name__ == "__main__":
    test_cases = [
        (['a', 'b', 'ba', 'bca', 'bda', 'bdca']),
        (['a', 'ba', 'zxb', 'bca', 'bda', 'bdca', 'zxbe', 'azxbe', 'azxpbe']),
        (['zxb', 'bca', 'bda', 'bdca', 'zxbe']),
        (['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']),
    ]
    answers = [
        4,
        4,
        2,
        10,
    ]

    for test_case, expected in zip(test_cases, answers):
        result = longestChain(test_case)
        assert result == expected, f"Expected {expected}, but got {result}"

    print("All test cases passed!")