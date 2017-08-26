"""

Usage:
    autograder.py <json> [options]

Options:
    --out=<out>     Output file [default: results.json]
"""

import docopt
import json


def main():
    arguments = docopt.docopt(__doc__)

    with open(arguments['<json>']) as f:
        data = json.load(f)

    total = 0.0
    for question_id in data['question_ids']:
        score = data[question_id]
        if not question_id.endswith('_text') and score.isnumeric():
            total += float(score)

    output = {
        'name': data['name'],
        'email': data['email'],
        'sid': data['sid'],
        'total': total
    }

    with open(arguments.get('--out', 'results.json'), 'w') as f:
        f.write(json.dumps({
            'output': json.dumps(output),
            'score': str(total)
        }))


if __name__ == '__main__':
    main()