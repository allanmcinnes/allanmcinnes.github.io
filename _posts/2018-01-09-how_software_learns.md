---
layout: post
published: true
title: How Software Learns
tags: [architecture, design, design principles, agile, bduf]
---

Software development approaches that "embrace change" have become immensely popular over the last couple of decades. Many software developers consciously avoid "Big Design Up Front" in favour of incrementally developing software story-by-story. But the idea of *"avoiding BDUF"* often mutates into an attitude that *"if you refactor often enough and a good software architecture will magically just happen"*. Architectural planning is seen as something that you do for big static things, like buildings, not for something dynamic, like software. But what if I told you that buildings are a lot more dynamic than you probably think? Can we learn something about software by looking at buildings?

Disclaimer: don't let the title fool you, this note is *not* about "machine learning".

## How Buildings Learn

[Stewart Brand's](https://en.wikipedia.org/wiki/Stewart_Brand) book [*"How Buildings Learn"*](https://en.wikipedia.org/wiki/How_Buildings_Learn) looks at how buildings evolve over time in response to changing user needs. It turns out that buildings evolve a lot. As Brand says (p. 178) :

> *"All buildings are predictions. All predictions are wrong."*

According to Brand, over a 50 year period the changes made to a building can cost *three times* as much as the original cost to put the building up. Sounds a little like "software maintenance" costs, doesn't it?

### "Shearing Layers"

Changes in a building occur at several different timescales. Brand suggests that a building can be conceptually split into 6 ["shearing layers"](https://en.wikipedia.org/wiki/Shearing_layers) that each represent a different timescale:

- _Site:_ the geographic environment of the building (effectively eternal)
- _Structure:_ the foundation and load-bearing elements, which are difficult and expensive to change (30-300 year life)
- _Skin:_ the external surfaces (20 year life)
- _Services:_ wiring, plumbing, networking, elevators, etc. (7-15 year life depending on technological changes)
- _Space Plan:_ internal partitioning (3-30 year life depending on what the building is used for)
- _Stuff:_ furniture, appliances, personal property, etc. (changes on timescales ranging from days to months)

Thinking in terms of these "shearing layers" can be helpful for understanding how to help buildings learn.

### Designing Buildings To Learn

Buildings that are able to learn evolve to meet changing needs without requiring costly demolition and replacement.

Keeping each of the shearing layers "decoupled" from the others allows changes to be made at their natural timescale without disrupting other layers. It's easier to move a stand-alone bookshelf than one that's built into a wall.

But decoupling isn't enough. Slow-changing layers control the changes possible in faster-changing layers. For example, the energy required by heating Services depends on the the Skin (reflectivity, insulation, etc.), which is in turn constrained by the Structure. The possible locations of your stand-alone bookshelf are constrained by the shape of the Space Plan.

Designing a building that can learn *well* involves anticipating likely (and unlikely) changes at different timescales, and trying to make sure that the slower layers support the potential changes at faster layers.

## How Software Learns

Of course, software isn't like a building. We expect software to change. The capability to change is a major part of what makes software valuable. It's why we call it *software*. The prevalent software development wisdom encourages designing for change.

But, drawing on Brand's ideas about buildings, perhaps there's some value in thinking about the varying *timescales* of software changes.

### "Shearing Layers" For Software

As a thought experiment, let me offer up a possible set of software "shearing layers":

- _Programming Language(s):_ rare to see this change once established.
- _Structure:_  major components and core abstractions (storage, UI, models, abstract devices, etc.), and the type of connections between them (direct calls, publish/subscribe, event-driven, etc.). Changes at this level are infrequent (timescale: years to decades).
- _OS/Platform/Libraries:_ changes to keep up with technology (timescale: years).
- _UI Look and Feel:_ influenced by choice of platform and libraries, but also by principles of user interface design and aesthetics. Often changed from one major version to the next version (timescale: 6 months to a year).
- _Features:_ the bread and butter of software change during the development lifecycle. Added or changed on a story-by-story basis (timescale: weeks to months).
- _User Configuration:_ day-to-day modifications to functionality made by end-users (timescale: hours to days).

I'm not claiming this set of layers is 100% right for all applications. But Foote and Yoder identify a similar set of layers in their classic [Big Ball of Mud](http://www.laputan.org/mud/) paper, so it's hopefully somewhere in the ballpark of "right". It should provide a reasonable starting point for thinking about the shearing layers that *are* applicable to your software.

### Designing Software To Learn?

It'd be nice if *every* aspect of our software was easy to change. But in practice we often end up making design choices that ease one kind of change while making other changes harder (the [expression problem](https://en.wikipedia.org/wiki/Expression_problem) is a classic example of this kind of situation).

Making some changes harder won't be a problem if the design choices we make keep the shearing layers decoupled, and ensure that slower layers support potential changes at faster layers. But as Foote and Yoder point out in their [Big Ball of Mud](http://www.laputan.org/mud/) paper:

> "When the SHEARING LAYERS that emerge as change drives the system's evolution run against the existing grain of the system, its structure can be undermined, and the result can be a BIG BALL OF MUD."

You *might* be able to reach a design that aligns with the shearing layers by refactoring as you go. But it'll require active effort to avoid sliding into that "Big Ball of Mud". And you're likely to find that even your refactoring is easier if you get the "grain of the system" aligned with the shearing layers from the start.

That doesn't mean "Big Design Up Front". No sense in designing down to the tiniest detail when you expect everything to change. Instead, I've found it useful to apply what I think of as ["Big Picture Design Up Front"](http://www.codingthearchitecture.com/2017/10/11/evolutionary_design_still_requires_up_front_thinking.html). Give some thought to the shearing layers in your software, and plan how to keep them decoupled. The result is software that *intentionally* embraces change, because it's designed from the start to *learn well*.
