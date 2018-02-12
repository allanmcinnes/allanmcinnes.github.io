---
layout: post
published: true
title: Decisions, Decisions
tags: [architecture, design, design process, document, agile, documentation, documenting, decisions, bduf, brooks, mythical man month, lightweight]
---

I've [argued in the past](https://allanmcinnes.github.io/2017/10/15/ilities-drive-architecture/) that it's worth putting some thought into the _why_ behind your design for a software architecture. But while knowing the _why_ at the time is great, it's even more helpful to be able to remember the _why_ a month or a year later. I was recently reminded of this when I stumbled across Doug Arcuri's post on [the importance of documenting software decisions](https://hackernoon.com/the-decision-hypothesis-aa512e0113).

## Docs or it didn't happen

Arcuri has been looking back through Fred Brooks' influential [Mythical Man-Month](https://www.pearson.com/us/higher-education/program/Brooks-Mythical-Man-Month-The-Essays-on-Software-Engineering-Anniversary-Edition-2nd-Edition/PGM172844.html), and draws out some lessons from Brooks about documenting software.

It's amazing how much of what Brooks talks about still rings true today. We're still struggling with incorporating documentation into the code and keeping it up to date (although most recent projects I've worked on extensively use tools like [Doxygen](https://www.stack.nl/~dimitri/doxygen/) to help with that). But probably the most important lesson from Brooks isn't about *how* to document. It's about *what* to document. Documenting *decisions* is of crucial importance.

That probably shouldn't be a surprise. You can view _design_ as the process of making _decisions_ about how to solve a problem. There are big decisions, like *"what is the problem we're trying to solve?"*, and small decisions, like *"what variable name should I use here?"*. [Design principles](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)) and [design patterns](https://en.wikipedia.org/wiki/Software_design_pattern) help us to make decisions that will lead to a good solution. Agile development practices often focus on [getting rapid feedback on the decisions](https://allanmcinnes.github.io/2016/09/08/getting-in-tune/) we've made.

And yet, when we look back later, it's not always clear _why_ we made particular decisions.

The question is, how can we remember the _why_? Code by itself records the _what_, but it does a poor job recording the _why_.

## A love-hate relationship

As both Brooks and Arcuri point out, we already know how to remember the _why_: *documentation!*

*Wait!* Don't leave yet!

Documentation may be the thing that every software developer loves to hate. But it's also what you love to have when you get dropped into a complex piece of source code written by some other team. And "documentation" doesn't have to mean "Big Design Up Front". Nor does it have to mean lots of boilerplate-heavy Word documents. Useful documentation should be low-effort to create, easy to incrementally keep up-to-date, and live as close to the software it documents as possible.

You probably already do some documentation. You document the _why_ behind low-level decisions directly in the code as comments. You can (should!) document module-level decisions, again in the code, using something like Doxygen or Javadocs.

But what about higher-level decisions? How (and where) can you document those in a lightweight way?

## Decision logs

For high-level design decisions, Arcuri recommends an approach he calls [DECISIONS.md](http://akazlou.com/posts/2015-11-09-every-project-should-have-decisions.html): a simple Markdown log of the _why_ behind key decisions that is incrementally updated, and stored in source control along with the code.

All of which sounds like a good idea. But what really struck me is that this idea sounds very similar to the notion of [Architecture Decision Records](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions), which I've been playing around with incorporating into projects for the last year or so.

ADRs provide a little more structure for documenting the _why_ than you'll find in DECISIONS.md, and ADRs split the decision log into separate timestamped files. But, aside from that, the two ideas are remarkably similar. That's probably an indication that there's an essential truth to be found here: an incrementally updated architecture decision log is a useful tool in complex software development projects.

## Why and how

So, be conscious of the _why_ behind your architecture-level design decisions. But also give some thought to *documenting* those decisions using something like DECISIONS.md or Architecture Decision Records. They're lightweight, incremental, compatible with agile approaches, and can help you (or another developer) understand _why_ your software architecture looks the way it does. Nat Pryce has even put together a [command-line tool](https://github.com/npryce/adr-tools) to help manage ADRs. The decisions behind it are, of course, [documented as ADRs](https://github.com/npryce/adr-tools/tree/master/doc/adr).
