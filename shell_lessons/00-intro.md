---
layout: lesson
root: .
title: The Unix Shell
subtitle: Introducing the Shell
minutes: 5
---
### Learning Objectives
*   Explain how the shell relates to the keyboard, the screen, the operating system, and users' programs.
*   Explain when and why command-line interfaces should be used instead of graphical interfaces.

# Working with the shell

Computers and humans can interact in many different ways. The earliest computers had to be rewired for every new set of commands. The most cutting-edge methods (which often seem to belong to sci-fi movies!) 
include direct brain-computer links and speech interfaces.
Since these are still in their infancy,
most of us are stuck using icons, windows, mice, and pointers to tell computers what we want them to do.
These technologies didn't become widespread until the 1980s,
but their roots go back to Doug Engelbart's work in the 1960s,
which you can see in what has been called
"[The Mother of All Demos](http://www.youtube.com/watch?v=a11JDLBXtPQ)".

## What is the command-line interface?
Between the 1950s and the 1980s, most users interacted with computers using keyboards and line printers. This was initially done using teleprinters (TTY machines), which literally printed onto paper each command sent by the user and the output produced by the computer. In the 1970s, as video displays became more widely available, this text dialog transitioned away from physical paper and onto screens.

This text-based method of interacting with a computer program is called a
**command-line interface**, or CLI. Even after the widespread adoption of **graphical user interfaces**, or GUIs, the command line continues to be extensively used by programmers and system administrators, as well as for many applications in engineering and scientific disciplines.

The command line is often the easiest way to interact with remote machines and supercomputers. 
Familiarity with the shell is near essential to run many specialized tools and resources, including high-performance computing systems. As clusters and cloud computing become more popular for scientific data crunching, being able to drive them using a command-line interface is becoming a necessary skill. 

## How does the command-line interface work?
The heart of a CLI is a **read-evaluate-print loop**, or REPL:
when the user types a command and then presses the enter (or return) key,
the computer reads it,
executes it,
and prints its output. When using a command-line interface, however, the user is not directly interacting with the guts of the computer. Both CLIs and GUIs are known as **shells** because they are programs that enclose the core of the operating system (the **kernel**) to hide much of its complexity and make it simpler for the user to interact with it.

When using a CLI, the interface is a program called a **command shell** that takes what the user types, figures out what commands to run, and orders the computer to execute them (while both CLIs and GUIs are technically shells, the command shell is commonly called *the shell*). The shell doesn’t perform any calculations itself. Instead, typing a command in the shell causes its corresponding computer program (also called an executable or script) to run and perform the desired actions.

## Using the command-line
The most popular shell for the Unix operating system is **Bash**,
the Bourne Again SHell
(so-called because it's derived from a shell written by Stephen Bourne --- this
is what passes for wit among programmers!). Bash is the default shell on most modern implementations of Unix, including MacOS and Linux,
and in most packages that provide Unix-like tools for Windows.

Using the shell to interact with the operating system feels differently than using the desktop environment (the GUI) of any of the popular operating systems. Shell commands are terse (often only a couple of characters long),
their names are frequently cryptic,
and their output is lines of text rather than something visual like a graph. While using the command line might sometimes feel cumbersome and unfamiliar, the shell allows us to combine existing tools in powerful ways with only a few keystrokes
and to set up scripts to handle large volumes of data automatically.

The command-line skills covered here will allow us to navigate the file system and to create and modify text files from the shell. These basic tasks can be combined and built upon to tackle a wide range of scientific questions and computational challenges.

## Nelle's Pipeline: Starting Point

Nelle Nemo is a first-year graduate student in marine biology. For her dissertation, she will be studying gelatinous marine life in the [Great Pacific Garbage Patch](http://en.wikipedia.org/wiki/Great_Pacific_Garbage_Patch). She just returned from a six-month survey of the
[North Pacific Gyre](http://en.wikipedia.org/wiki/North_Pacific_Gyre), and she brought back a first batch of 300 individual samples.

She now needs to:

1.  Run each sample through an assay machine
    that will measure the relative abundance of 300 different proteins.
    The machine's output after processing a single sample is
    a text file with one line of data for each of the proteins.
2.  Calculate statistics for each of the proteins separately
    using a program her supervisor wrote called `goostat`.
3.  Compare the statistics for each protein
    with the corresponding statistics for every other protein
    using a program that a former graduate student in her lab wrote called `goodiff`.
4.  Write up her results.
    Her supervisor would really like her to do this by the end of the month
    so that her paper can appear in an upcoming special issue of *Aquatic Goo Letters*.

It takes about half an hour for the assay machine to process one sample.
The good news is that it only takes two minutes to set up an individual sample to run.
Since her lab has eight assay machines that she can use in parallel,
analyzing her 300 samples should "only" take about two weeks.

After she finishes processing all of her samples, she has to analyze the data files that the assay machines produced. If she has to run `goostat` and `goodiff` by hand, however, 
she'll have to enter filenames and click "OK" at least 45,150 times
(300 runs of `goostat`, plus 300 x 299 / 2 runs of `goodiff`).
At 30 seconds each,
that will take more than two weeks and cause her to miss her paper deadline. Also, the chances of her typing all of those commands correctly are practically zero, so it is likely that she will accidentally introduce errors to her results and will have to re-do some of her work.

The next few lessons will explore what she should do to avoid having to process all of her data by hand.
More specifically,
they explain how she can use a command shell
to automate the repetitive steps in her processing pipeline
so that her computer can work 24 hours a day while she writes her paper.
As a bonus,
once she has put a processing pipeline together,
she will be able to use it again whenever she collects more data. Automating the data analysis will not only reduce her workload but it will also guarantee that the process remains consistent and reproducible throughout her graduate career.

