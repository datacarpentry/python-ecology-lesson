# Contributing New Material

Data Carpentry is an open source project, and we welcome contributions of all
kinds: new and improved lessons, bug reports, and small fixes to existing
material are all useful.

By contributing, you are agreeing that Data Carpentry may redistribute your
work under [these licenses](LICENSE.md).


**Table of Contents**

- [Working With GitHub](#working-with-github)
- [Locations and Formats](#locations-and-formats)
- [Formatting of the material](#formatting-of-the-material)
- [Suggestions for Instructor Checkout](#suggestions-for-instructor-checkout)
- [FAQ](#faq)


## Working With GitHub

1.  Fork the `datacarpentry/lesson-name` repository on GitHub.

2.  The default branch in our lessons is `gh-pages`. Create a
    new branch for your changes.
    Give your branch a meaningful name,
    such as `fixing-typos-in-shell-lesson`
    or `adding-tutorial-on-visualization`.

3.  Clone this repository and branch to work with it on your computer.
    git clone the repository with -b 'branch name'

4.  Make your changes, commit them, and push them to your repository on GitHub.

5.  Send a pull request to the `gh-pages` branch of the main datacarpentry
    repository at http://github.com/datacarpentry/lesson-name. This can
    be done through the github web interface.

If it is easier for you to send them to us some other way,
please mail us at
[admin@datacarpentry.org](mailto:admin@datacarpentry.org).
Given a choice between you creating content or wrestling with Git,
we'd rather have you doing the former.


## Locations and Formats

Every lesson has a repository of its own, while individual topics are files
in that directory.  For example, the `python-ecology-lesson` repo containing our
introduction to Python using ecology data contains the files
`00-short-introduction-to-Python.md`,
`01-starting-with-data.md` and so on.  (We use two digits followed by a short
topic key to ensure files appear in the right order when listed.)

Lessons may be written in Markdown, as Jupyter Notebooks, or in other formats.
However, as explained in [the README file](README.md), Jekyll (the tool GitHub
uses to create websites) only knows how to handle Markdown and HTML.  If some
other format is used, the author of the lesson must add the generated Markdown
to the repository.  This ensures that people who *aren't* familiar with some
format don't have to install the tools needed to work with it (e.g., R
programmers don't have to install the Jupyter Notebook).


## Formatting of the material

To ensure a consistent formatting of the lessons, we recommend the following
guidelines:

- No trailing white space
- Wrap lines at 80 characters (unless it breaks URLs)
- Use unclosed [atx-style headers](http://spec.commonmark.org/0.25/#atx-headings)
- For Python code adhere to Style Guide defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/)


## Suggestions for Instructor Checkout

- [ ] Check links on setup [and install webpage](http://www.datacarpentry.org/python-ecology-lesson/).
- [ ] Check for presence of all "required" folders and csvs. We did some
  remodeling, and there might be references that need scrubbing.
- [ ] Attendees have asked for a little more data manipulation and sorting.
- [ ] The plotting lesson could really use some love, and a discussion of
  exporting high-quality plots.
- [ ] Lesson 7 repeats some matplot content, but with a new dataset. Rework to
  use the previous lesson data.
- [ ] The column name `plot_id` in surveys.csv confused a few participants who
  didn't think of the word `plot_id` in terms of land, but in terms of a
  drawing. Consider a rename to `site_id`.
- [ ]  The 'short introduction to python' lesson overlaps quite a bit with the
  'data types and format' lesson when it comes to datatypes. Look over and
  eliminate overlap.
- [ ] Read over challenges for precision, and check that the answers in the
  (brand-new!) instructor guide make sense.


## FAQ

-   *Where can I get help?*
    <br/>
    Mail us at [admin@datacarpentry.org](mailto:admin@datacarpentry.org)

