from flask import Flask, render_template, request
import enchant
from itertools import permutations, combinations


puzzle_app = Flask(__name__)


@puzzle_app.route('/')
def index():
    return render_template('index.html')


@puzzle_app.route('/results', methods=['GET', 'POST'])
def results(f_anagrams=None, inp=None, f=None, w=None):

    en_US = enchant.Dict("en_US")

    anagrams = []
    inp = str(request.form['word']).lower()

    i = 2
    while (i <= (len(inp))):
        com = [''.join(x) for x in combinations(inp, i)]

        for j in com:
            perm = [''.join(p) for p in permutations(list(j))]

            for k in perm:
                if en_US.check(k) and (k != inp) and (k not in anagrams):
                    anagrams.append(k[:])
        i += 1

    f = len(anagrams)
    if (f > 1):
        w = "words"
    else:
        w = "word"
    return render_template('results.html', anagrams=anagrams, inp=inp, f=f)


if __name__ == '__main__':
    puzzle_app.run(debug=True)
