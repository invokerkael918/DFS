from collections import deque


class Solution2:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        indexes = self.build_indexes(dict)

        distance = self.bfs(end, indexes)

        results = []
        self.dfs(start, end, distance, indexes, [start], results)

        return results

    def build_indexes(self, dict):
        indexes = {}
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i + 1:]
                if key in indexes:
                    indexes[key].add(word)
                else:
                    indexes[key] = set([word])
        return indexes

    def bfs(self, end, indexes):
        distance = {end: 0}
        queue = deque([end])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexes):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
        return distance

    def get_next_words(self, word, indexes):
        words = []
        for i in range(len(word)):
            key = word[:i] + '%' + word[i + 1:]
            for w in indexes.get(key, []):
                words.append(w)
        return words

    def dfs(self, curt, target, distance, indexes, path, results):
        if curt == target:
            results.append(list(path))
            return

        for word in self.get_next_words(curt, indexes):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, indexes, path, results)
            path.pop()


class Solution1:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}

        self.bfs(end, start, distance, dict)

        results = []
        self.dfs(start, end, distance, dict, [start], results)

        return results

    def bfs(self, start, end, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words

    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return

        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()
