# Self Grading Infrastructure

self-grading HTML generator and Gradescope autograder

* Generates self-grading form from LaTeX
* Self-grading form automatically generates and downloads JSON file

# Installation

Install Python packages via `pip`.

```
pip -r requirements.txt
```

# HTML v1 Usage

In `v1`, each homework has its own self-grade HTML form. To generate a self-grade form, use the `html/create_form.py` script.

```
cd html
python create_form.py path/to/tex
```

The script by default looks for `\Question{...}` commands, and for each question, looks for `\Part` commands. The outputted file is saved to the current directory. 

# HTML v2 Usage

In `v2`, one self-grade HTML form is used for all homeworks, `html/self_grade.html`. Each homework's "self-grade form" is just a different URL, or queryparams, for that one self-grade form. To generate a link, use the `html/create_link.py` script.

```
cd html  # if you haven't already
python create_link.py path/to/tex
```

This script works the same way v1 did.

# Gradescope Autograder

Simply zip the `autograder/` directory's contents, and upload to the relevant Gradescope autograder configuration. The script simply adds up the score.