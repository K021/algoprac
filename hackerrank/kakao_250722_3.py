from collections import defaultdict, deque

def getSubTeams(existingTeamEdges, queries):
    adj = defaultdict(list)
    for a, b in existingTeamEdges:
        adj[a].append(b)
        adj[b].append(a)  # Bidirectional edges for traversal
    
    tree = defaultdict(list)
    deleted = set()
    ret = []

    root = 'team-1'  # Assuming 'team-1' is the root of the tree
    visited = set()
    q = deque([root])

    # BFS to build the initial tree structure
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        for child in adj[node]:
            if child not in visited:
                tree[node].append(child)
                q.append(child)
    
    def create_team(parent, child):
        if parent not in deleted:
            tree[parent].append(child)
        # print(f"Created team {child} under {parent}")
        # print(f"Current tree: {tree}")
        # print(f"Deleted teams: {deleted}")
        # print()

    def delete_team(to_delete):
        if to_delete not in deleted:
            stack = deque([to_delete])
            while stack:
                node = stack.pop()
                deleted.add(node)
                for child in tree[node]:
                    stack.append(child)
            # print(f"Deleted team {to_delete} and its subteams")
            # print(f"Current tree: {tree}")
            # print(f"Deleted teams: {deleted}")
            # print()

    def count_teams(root):
        ret.append(count_subtree(root))
        # print(f"Counted teams under {root}: {ret[-1]}")
        # print(f"Current tree: {tree}")
        # print(f"Deleted teams: {deleted}")
        # print(f"Current result: {ret}")
        # print()

    def count_subtree(node):
        if node in deleted:
            return 0
        count = 1
        for child in tree[node]:
            count += count_subtree(child)
        return count
    
    command_func = {
        "create_team": create_team,
        "delete_team": delete_team,
        "count_teams": count_teams,
    }
    
    for q in queries:
        args = q.split()
        command_func[args[0]](*args[1:])
    
    return ret
        
        

if __name__ == '__main__':
    test_cases = [
        (
            [['team-1', 'team-2'], ['team-2', 'team-3'], ['team-2', 'team-4']],
            ['create_team team-1 team-5', 'count_teams team-2', 'count_teams team-1'],
        ),
        (
            [['team-2', 'team-4'], ['team-1', 'team-2'], ['team-1', 'team-3']],
            ['count_teams team-2', 'count_teams team-1', 'count_teams team-3'],
        ),
        (
            [['team-3', 'team-4'], ['team-1', 'team-4'], ['team-3', 'team-2']],
            ['create_team team-1 team-5', 'count_teams team-5', 'delete_team team-5', 'count_teams team-2', 'count_teams team-4', 'delete_team team-2', 'delete_team team-4', 'count_teams team-1', 'count_teams team-1', 'create_team team-1 team-6'],
        ),
        (
            [['team-1', 'team-6'], ['team-1', 'team-8'], ['team-8', 'team-4'], ['team-1', 'team-7'], ['team-1', 'team-2'], ['team-7', 'team-5'], ['team-7', 'team-9'], ['team-7', 'team-3']],
            ['delete_team team-6', 'create_team team-8 team-10', 'delete_team team-8', 'count_teams team-1', 'count_teams team-3', 'create_team team-9 team-11', 'create_team team-9 team-12', 'count_teams team-9', 'create_team team-5 team-13', 'create_team team-13 team-14'],
        ),
        (
            [['team-5', 'team-2'], ['team-5', 'team-9'], ['team-2', 'team-6'], ['team-6', 'team-3'], ['team-6', 'team-8'], ['team-8', 'team-10'], ['team-9', 'team-4'], ['team-1', 'team-8'], ['team-4', 'team-7']],
            ['count_teams team-2', 'delete_team team-2', 'count_teams team-6', 'create_team team-10 team-11', 'count_teams team-3', 'create_team team-3 team-12', 'delete_team team-8', 'count_teams team-1', 'create_team team-1 team-13', 'create_team team-13 team-14'],
        ),
    ]
    answers = [
        [3, 5],
        [2, 4, 1],
        [1, 1, 3, 1, 1],
        [6, 1, 3],
        [5, 2, 1, 1],
    ]

    for test_case, expected in zip(test_cases, answers):
        result = getSubTeams(*test_case)
        assert result == expected, f"Expected {expected}, but got {result}"

    print("All test cases passed!")