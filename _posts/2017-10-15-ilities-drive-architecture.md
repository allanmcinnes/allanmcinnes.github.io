---
layout: post
published: false
title: Ilities Drive Architecture
---

Why do we structure a software design the way we do? 

For that matter, why do we structure a design at all? 

If all we cared about was the mapping from software inputs to software outputs, then an internal design that looked liked spaghetti would be just fine.
<center><img src="/images/spaghetti.png" width="300" alt="Spaghetti architecture"/></center>
Of course, we *do* impose a structure on our designs. We split things into functions, objects, and modules. But why? Clearly there's more at work here than just input/output requirements.
<center><img src="/images/structure.png" width="300" alt="Structured architecture"/></center>

## Structure is architecture

The architectural level of a design lets us see *how* the system will do whatever it's supposed to do without getting bogged down in all of the low-level details--like looking at the shape of rooms in a building without worrying about the exact shape of the electrical outlets. Taking this kind of abstract view is a classic technique for dealing with the cognitive complexity of large designs. For example, a microprocessor is constructed from billions of transistors, but we tend to think of the processor design in terms of arithmetic logic units, memory, registers, and other abstract components.

When we're talking about software, the architecture describes the high-level components we build the software from (modules, libraries, databases, etc.), and the way that those components are connected to each other. Your software *will* have an architecture, whether you plan it or not. Maybe it's worth giving that architecture some conscious thought.

## But why?

Think back to your last software development project. Did you think about architecture at all? If you did, can you explain *why* you chose the components that you did?

If you're like a lot of software developers, you may have broken your design down into components that are responsible for separate "major functions". 

Perhaps you tried to "hide" key design decisions within individual components, which is characteristic of modern object-oriented design and is the goal of many design patterns.

You probably also used a bunch of off-the-shelf components (libraries or frameworks, perhaps even entire third-party applications). 

And maybe, if you thought about architecture, you used one of the classic architectural patterns: layers, pipes-and-filters, a blackboard.

## No, really, why?

But *why* did you do things that way?

I'd argue that, even if you didn't think about it consciously, a lot of your design was driven by various *"-ilities"*: the qualities of your system that your trying to achieve along with meeting the functional requirements.

Much of your architecture was probably driven by a concern for *understandability*. A functional decomposition isn't *necessary* to meet the functional requirements. But decomposing things that way makes it easier to understand how and why individual functional requirements are met. Certainly eaasier to udnerstand than spaghetti.

Hiding design decisions is an approach advocated in David Parnas' seminal paper on software design, [*"On the Criteria to be Used in Decomposing Systems into Modules"*](http://repository.cmu.edu/cgi/viewcontent.cgi?article=2979&context=compsci), in which he argues against functional decomposition and proposes using *changeability* as a criterion for structuring a design.

Using well-known architectural patterns inevitably enhances *understandability*, since anyone looking at the system will know what to expect. Individual architectural patterns also support other qualities. For example, a layered architecture supports *changeability* through hiding design decisions within layers.

And what about those off-the-shelf components you used? Why not write everything from scratch? You were probably motivated by things like the *affordability* of the required work, and the *feasbility* of meeting your schedule.

## It's all about the -ilities

Seeing architecture as being driven by -ilities is a viewpoint espoused by Len Bass, Paul Clements, and Rick Kazman in the book [Software Architecture in Practice](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30264). I think it's a useful viewpoint, because it makes you stop and consider *why* your architecture looks the way it does.

Is a layered architecture *always* the best choice? It depends on what -ilities you're really interested in. Maybe it makes sense to violate the layering to support other -ilities (a performance-related quality, perhaps). By thinking about those -ilitites you can make that decision in a principled way.

What about your use of off-the-shelf components? How did you make your "make vs buy" decision? Were there other criteria in play aside from affordability? Have you considered maintainability or interoperability? Again, you can approach the make/buy decision in a principled way.

Perhaps most importantly, looking at the architecture from the perspective of -ilities can help you think about the -ilities you should consider but haven't yet. How important is reliability to your system? Have you given any thought to preserving confidentiality (a key security property)? What about the usability of your interface?

So, next time you look at the architecture of your software (either a new deisgn, or your existing project), ask yourself "what are the key -ilities here?" You may find some ways to make your architecture better. And you'll have a much better odea of whay your software is struectured the way it is.
