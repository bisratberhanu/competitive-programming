# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

def findAllPeople(n, meetings, firstPerson):
    knows_secret = set([0, firstPerson])
    meetings.sort(key=lambda x: x[2])  # Sort meetings by time

    for time, group in groupby(meetings, key=lambda x: x[2]):
        uf = UnionFind(n)  # Reset Union-Find for each time slot
        temp_meetings = list(group)
        for x, y, _ in temp_meetings:
            uf.union(x, y)

        # Find all people connected to the secret holders for this time slot
        connected_to_secret = set()
        for person in range(n):
            if uf.find(person) in knows_secret or person in knows_secret:
                connected_to_secret.add(person)

        # Update knows_secret for the next time slot
        knows_secret = connected_to_secret

    return list(knows_secret)
