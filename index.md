---
layout: lesson
root: .
title: "Data Carpentry: Python for Ecologists"

contributors:
  - April Wright
  - Ethan White
  - John Gosset
  - Leah Wasser
  - Mariela Perignon
  - Tracy Teal

maintainers:
  - April Wright
  - John Gosset
  - Mateusz Kuzak

software: Python
---

**Content Contributors:** {{ page.contributors | join: ', ' }}

**Lesson Maintainers:** {{ page.maintainers | join: ', ' }}

Data Carpentry's aim is to teach researchers basic concepts, skills, and tools
for working with data so that they can get more done in less time, and with less
pain. The lessons below were designed for those interested in working with
ecological data in Python.


## Lessons

- [Short Introduction to Python](00-short-introduction-to-Python)
- [Starting With Data](01-starting-with-data)
- [Index Slice Subset](02-index-slice-subset)
- [Data Types and Format](03-data-types-and-format)
- [Merging Data](04-merging-data)
- [Data Analysis Automation: Loops and Functions](05-loops-and-functions)
- [Plotting with ggplot](06-visualization-ggplot-python)
- [Putting It All Together](07-putting-it-all-together)
- [Accessing SQL using Python](08-working-with-sql)


## Data

Data for this lesson is from the Portal Project Teaching Database -
[available on FigShare](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).

Specifically, the data files we use in these lessons are:

- [surveys.csv](https://ndownloader.figshare.com/files/2292172)
- [species.csv](https://ndownloader.figshare.com/files/3299483)


## Requirements

Data Carpentry's teaching is hands-on, so participants are encouraged to use
their own computers to insure the proper setup of tools for an efficient workflow.
*These lessons assume no prior knowledge of the skills or tools*, but working
through this lesson requires working copies of the software described below.
To most effectively use these materials, please make sure to install everything
*before* working through this lesson.

Participants are required to abide by Data Carpentry's
[Code of Conduct](http://www.datacarpentry.org/code-of-conduct/).


{% if page.software == "Python" %}
{% include pythonSetup.html %}
{% elsif page.software == "Spreadsheets" %}
{% include spreadsheetSetup.html %}
{% elsif page.software == "R" %}
{% include rSetup.html %}
{% else %}
{% include anySetup.html %}
{% endif %}


## Acknowledgements & Support

Data Carpentry is supported by the [Gordon and Betty Moore Foundation] and a
partnership of several NSF-funded [BIO] Centers ([NESCent], [iPlant], [iDigBio],
[BEACON] and [SESYNC]) and [Software Carpentry], and is sponsored by the [Data
Observation Network for Earth] (DataONE). The structure and objectives of the
curriculum as well as the teaching style are informed by [Software Carpentry].


[Gordon and Betty Moore Foundation]: https://www.moore.org
[BIO]: https://www.nsf.gov/dir/index.jsp?org=BIO
[NESCent]: https://nescent.org
[iPlant]: http://www.iplantcollaborative.org
[iDigBio]: https://www.idigbio.org
[BEACON]: http://beacon-center.org
[SESYNC]: https://sesync.org
[Software Carpentry]: https://software-carpentry.org
[Data Observation Network for Earth]: https://www.dataone.org
