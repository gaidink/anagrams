from flask import Flask, render_template, request
import enchant
from itertools import permutations, combinations


puzzle_app = Flask(__name__)


@puzzle_app.route('/')
def index():
    return render_template('index.html')


@puzzle_app.route('/results', methods=['GET', 'POST'])
def results(f_anagrams=None, k=None, inp=None, found=None):

    en_US = enchant.Dict("en_US")

    anagrams = []
    f_anagrams = []
    inp = str(request.form['word'])
    k = int(request.form['word_len'])

    com = [''.join(x) for x in combinations(inp, k)]

    for i in com:
        perm = [''.join(p) for p in permutations(list(i))]

        for i in perm:
            if en_US.check(i) and (i != inp):
                anagrams.append(i)
    for i in anagrams:
        if i not in f_anagrams:
            f_anagrams.append(i[:])

    found = len(anagrams)
    return render_template('results.html', f_anagrams=f_anagrams, k=k, inp=inp, found=found)


if __name__ == '__main__':
    puzzle_app.run(debug=True)
