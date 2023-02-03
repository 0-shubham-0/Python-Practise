def bestTeamScore(scores, ages):
    n = len(scores)
    a = sorted(zip(ages,scores))
    sorted_scores=[x[1] for x in a]
    dp=[0 for _ in a]
    for i in range(n):
        dp[i]=sorted_scores[i]
        for j in range(i):
            if sorted_scores[j]<=sorted_scores[i]:
                dp[i]=max(dp[i],sorted_scores[i]+dp[j])
    return max(dp)
        
    

scores,ages = [20,3,5,10,15], [1,10,3,4,5]
bestTeamScore(scores,ages)
