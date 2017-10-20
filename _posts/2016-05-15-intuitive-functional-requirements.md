---
layout: post
published: true
title: More Intuitive Software Requirements?
---
I recently came across an interesting paper that got me thinking about how people naturally explain the kind of complex behaviors we expect from software. The paper is [*"Studying the Language and Structure in Non-Programmers’ Solutions to Programming
Problems"*](http://alumni.cs.ucr.edu/~ratana/PaneRatanamahatanaMyers00.pdf), by John F. Pane, Chotirat "Ann" Ratanamahatana and Brad A. Myers of Carnegie-Mellon University, and is part of CMU's ["Natural Programming" Project](https://www.cs.cmu.edu/~NatProg/). The focus of the paper is on how non-programmers tackle programming tasks. But the findings presented in this paper are probably as, or more, applicable to software functional requirements as they are to software implementation. After all, the audience for functional requirements should include not just experienced software developers, but customers, product owners, testers, and other people who aren't necessarily attuned to thinking like programmers.

The paper reports on a study that examined how programming tasks were tackled by children, aged 10-11 years, that had no prior programming experience. The children were given several tasks that involved describing, in their own words and pictures, how they would tell a computer to perform various scenarios from the classic PacMan game. The responses from each child were analyzed by independent raters who categorized and scored the individual elements of each child's response. And that's where things get interesting. Because those categories included things like "programming style" (e.g., imperative, declarative, event-based), "operations on multiple objects", and "remembering state". Here are the results for those categories:

* *Programming Style*: 54% of the response statements were "event-based", meaning that they involved describing behavior by explaining what should happen *when* (or *if*, or *after*) some event occurred. For example, *"When PacMan eats all the dots, he goes to the next level."*. Of the remaining statements, 18% expressed behavior constraints, such as *"PacMan cannot go through a wall"*, and 16% were declarative properties, such as *"There are 4 monsters"*. Only 12% involved sequential or imperative descriptions.
* *Operations on Multiple Objects*: 95% of statements involving operations on more than one object used set or subset descriptions (*"When PacMan eats all the dots..."*). Only 5% used explicit iteration or looping.
* *Remembering State*: Only 11% of statements used an explicit state variable to explain how a past action should affect a current action. The rest used some simply made some kind of reference to the previous event or action (e.g., *"When PacMan eats a special dot he is able to eat the ghosts."*)

What can we take away from these results? I see a few interesting things (caveats below).

1. Behavior constraints can be converted to an event-based description by slightly rephrasing them into a *When/Then* form (e.g., *"When PacMan tries to go through a wall..."*), which has the advantage of making them testable. That means that almost 75% of the behavior descriptions were either event-based, or easily convertible to an event-based form. It seems reasonable to infer that an event-based description of behavior is a fairly natural, or intuitive, way to explain what something should do. That's the *When/Then* in the *Given/When/Then* structure that I've [mentioned previously](https://allanmcinnes.github.io/2016/03/06/writing-software-functional-requirements/) as being a good way to phrase software functional requirements.
2. I've seen some requirements documents that specify loops or other iteration. Not only is explicitly requiring iteration probably an over-constraining specification of requirements, it's not particularly intuitive for non-programmers. When writing requirements, we're probably much better off explaining things in terms of sets and subsets (e.g., *"...Then an email is sent to all valid addresses"* instead of *"...iterate over the email addresses and send an email to each valid email address"*).
3. Non-programmers are less likely to think in terms of states than programmers are. Of course, I think [states shouldn't be in requirements](https://allanmcinnes.github.io/2016/05/01/state-in-requirements/) anyway. But my opinion about states was mostly to do with feeling that they over-constrained the design. The results in this study make me think that they may also simply be confusing for some people. Which would some to be yet another reason to write *Givens* in terms of previously observed events, just like the kids in this study did.

The caveat, of course, is that this is just one data point based on a relatively small study. And I suppose there's a further caveat that we may be seeing confirmation bias at work here: the paper says things that happen to agree with my current opinions, so it naturally gets my attention. Nevertheless, these seem like interesting results, and provide some food for thought even if they don't give conclusive guidance on how to produce more intuitive requirements. How well do your requirements line up with the way these kids tried to explain what a computer should do? And how easy does your programming language make it to translate those requirements into an implementation?