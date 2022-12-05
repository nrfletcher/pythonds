from graph import Graph

""" The word ladder problem is a classic graph algorithm problem which involves the challenge of converting
    one word to another word with two rules in mind:
        1. You may only change one letter of the word at a time
        2. At all points the intermediary word must be a valid word (real word)
        
    The goal is to find the least amount of changes required to convert from one word to another word using these
    two rules as way to utilize our graph data structure for conversion """


def graph_builder(file):
    d = {}
    g = Graph()
    wfile = open(file, 'r')

    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g


print(graph_builder('words.txt'))
