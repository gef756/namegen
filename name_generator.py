import argparse
import random


class NameGenerator:

    def __init__(self, adj_file='adjectives.txt', noun_file='pokemon151.txt',
                 sep='', seed=None):
        self.adj_list = self.parse_list(adj_file)
        self.noun_list = self.parse_list(noun_file)
        self.sep = sep
        random.seed(seed)

    @staticmethod
    def parse_list(file_name):
        with open(file_name, 'r') as f:
            res = f.read().splitlines()
        return res

    def generate_names(self, n):
        res = []
        for _ in xrange(n):
            res.append(self.generate_name())
        return res

    def generate_name(self):
        adj = random.choice(self.adj_list)
        noun = random.choice(self.noun_list)
        return adj.title() + self.sep + noun.title()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate random names'
                                                 'based on an adjective'
                                                 'and noun list')
    parser.add_argument('--n', dest='n', help='number of names to generate',
                        default=1)
    parser.add_argument('--sep', dest='sep', help='separator between '
                                                  'adjective and noun',
                        default='')
    parser.add_argument('--adjs', dest='adj', help='file with adjectives',
                        default='adjectives.txt')
    parser.add_argument('--nouns', dest='noun', help='file with adjectives',
                        default='pokemon151.txt')
    parser.add_argument('--seed', dest='seed', help='seed for random '
                                                    'generator')
    args = parser.parse_args()
    gen = NameGenerator(adj_file=args.adj, noun_file=args.noun,
                        sep=args.sep, seed=args.seed)
    names = gen.generate_names(int(args.n))
    for name in list(names):
        print name

