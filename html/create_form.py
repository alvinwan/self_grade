import jinja2
import sys
import os

arguments = sys.argv
filename = arguments[1]

with open(filename) as f:
    tex = f.read()

questions = []
question_ids = ['name', 'email', 'sid', 'duration_homework', 'duration_grade']
context = {'questions': questions}

questions_tex = tex.split('\\Question')
for id_, question in enumerate(questions_tex[1:]):
    num_parts = question.count('\Part')
    for part in range(num_parts):
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

context['question_ids'] = '"%s"' % '","'.join(question_ids)
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
out_path = os.path.basename(filename.replace('.tex', '.html'))
with open(out_path, 'w') as f:
    f.write(env.get_template('template.html').render(context))

