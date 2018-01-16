"""

Usage:
    autograder.py <json> [options]

Options:
    --out=<out>     Output file [default: /autograder/results/results.json]
"""

import docopt
import json
import os
import glob

def main():
    arguments = docopt.docopt(__doc__)
    try:
        autograde(arguments['<json>'], arguments['--out'])
    except UserWarning as e:
        output = {'error': e.message}
        with open(arguments['--out'], 'w') as f:
            json.dump({
                'output': json.dumps(output),
                'score': 0
            }, f)

def autograde(path, out):
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        pattern = os.path.join(os.path.dirname(path), '*.json')
        matches = list(glob.iglob(pattern))
        if len(matches) < 1:
            raise UserWarning('Submission should be a .json file.')
        path = matches[0]
        print(' * Could not find `self_grades.json`. Trying %s' % path)
        with open(path, encoding='utf-8') as f:
            data = json.load(f)

    total = 0.0
    for question_id in data['question_ids']:
        score = data[question_id]
        if (question_id.isdigit() or question_id.count('_') == 1) and score.isnumeric():
            total += float(score)

    output = {
        'name': data['name'],
        'email': data['email'],
        'sid': data['sid'],
        'total': total
    }

    with open(out, 'w') as f:
        json.dump({
            'output': json.dumps(output),
            'source': path,
            'score': str(total)
        }, f)


if __name__ == '__main__':
    main()
