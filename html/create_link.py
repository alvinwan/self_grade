import sys


def main():
    arguments = sys.argv
    filename = arguments[1]
    base_url = arguments[2] if len(arguments) > 2 else 'http://eecs189.org/self_grade'
    print(create_link(filename, base_url=base_url))


def create_link(filename, base_url='http://eecs189.org/self_grade'):
    with open(filename) as f:
        tex = f.read()

    questions = []
    question_ids = ['name', 'email', 'sid', 'duration_homework', 'duration_grade']

    questions_tex = tex.split('\\Question')
    for id_, question in enumerate(questions_tex[1:], start=1):
        num_parts = question.count('\Part')
        for part in range(num_parts):
            part += 1
            questions.append({
                'title': 'Question %d Part %d' % (id_, part),
                'id': "%d_%d" % (id_, part)
            })
            question_ids.append("%d_%d" % (id_, part))
            question_ids.append("%d_%d_text" % (id_, part))
        if num_parts == 0:
            questions.append({
                'title': 'Question %d' % id_,
                'id': str(id_)
            })
            question_ids.append(str(id_))
            question_ids.append(str(id_) + "_text")

    url = base_url + '?question_ids=%s' % ','.join([q['id'] for q in questions])
    return url


if __name__ == '__main__':
    main()