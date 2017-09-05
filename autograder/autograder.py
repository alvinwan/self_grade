"""

Usage:
    autograder.py <json> [options]

Options:
    --out=<out>     Output file [default: /autograder/results/results.json]
"""

import docopt
import json


def main():
    arguments = docopt.docopt(__doc__)

    with open(arguments['<json>'], encoding='utf-8') as f:
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

    with open(arguments['--out'], 'w') as f:
        json.dump({
            'output': json.dumps(output),
            'score': str(total)
        }, f)


if __name__ == '__main__':
    main()