# Software Papers as Software Modules

**How citing a software paper could include importing its code**

Andreas Zeller, CISPA / Saarland University

## The Reproducibility Problem

The difficulty to reproduce, reuse, or extend scientific results has long been a common concern in scientific circles.  The problem is the more troubling as computer software is commonly used to evaluate or even embody research results - and while one may assume that computer software should be far easier to copy and extend, most scientific software is not in a shape that others could work with it.  Even in computer science, where the majority of all publications describe some software or algorithm, only a small minority of papers actually makes this software available to others.

Many reasons are cited against making software available, mostly the fear and cost of having to support some huge infrastructure.  And yes, if you have implemented, say, a symbolic analysis for FORTRAN-77, you will end up with a huge mess of code that will be hard to maintain.  On the other hand, there will be a few key contributions your analysis will have made - the key contributions you would like to detail in your paper, possibly with pseudocode.  The question is: Aren't these key contributions worthwhile not only to be read, but also to be _used_ and _reused_?

In this paper, I will argue that papers can be organized _together with the software they describe_; even further, I will argue for an ecosystem in which papers can not only cite the work they build upon, but actually _use, reuse, and extend existing work_ in the same way software modules use, reuse, and extend each other.  And the good news is: Almost all ingredients for this do already exist.

* [Read the rest of the paper here](https://github.com/andreas-zeller/papers-as-modules/blob/master/Papers-as-Modules.ipynb)

* [Interact with the paper in Binder here](https://mybinder.org/v2/gh/andreas-zeller/papers-as-modules.git/master?filepath=Papers-as-Modules.ipynb)
