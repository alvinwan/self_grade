# Self Grading Infrastructure

self-grading HTML generator and Gradescope autograder

* Generates self-grading form from LaTeX
* Self-grading form automatically generates and downloads JSON file

# Installation

Install Python packages via `pip`.

```
pip -r requirements.txt
```

# HTML Usage

To generate a self-grade form, use the `html/create_form.py` script.

```
cd html
python create_form.py path/to/tex
```

The script by default looks for `\Question{...}` commands, and for each question, looks for `\Part` commands. The outputted file is saved to the current directory. 

# Gradescope Autograder