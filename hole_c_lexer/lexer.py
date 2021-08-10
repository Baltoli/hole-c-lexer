from pygments.lexer import inherit, words
from pygments.lexers.c_cpp import CLexer
from pygments.token import *

class HoleCLexer(CLexer):
    name = 'HoleC'
    aliases = ['holec']
    filenames = ['*.holec']

    tokens = {
        'statements': [
            (words(
                ('{?}', '??')),
                Generic.Deleted),
            (r'?T\d+', Generic.Deleted),
            inherit,
        ]
    }
