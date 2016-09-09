---
layout: post
published: true
title: Getting In Tune With Requirements
---

Requirements define what software should do. That's pretty easy to understand. What can be harder to understand is what the requirements actually imply about how the software will behave once its implemented.

## Notable requirements

The (admittedly imperfect) analogy that I like to use is that *requirements* are to *software* as a *score* is to an *orchestral performance*. A talented musician may be able to look at a score and understand what it will sound like when performed. But, to most of us, sheet music looks like a bunch of blobs and lines that are suggestive (*"I can see a rising pitch there"*), but don't give us a full understanding of what the music will sound like.

Now, would we expect a movie director to approve the music for a movie based on looking at the score? Of course not. They'd probably want to hear what the music sounded like, even if it was a partial rendition with only a few instruments. Then they could give useful feedback, like *"I really like the way the mood builds through that section, but I need the tension to peak right where those violins come in"*. That way when the full orchestra performs the score it's more likely that what they're performing is what the director needs.

## Music to a client's ears

Just as a movie director can't make a decision just by looking at a score, in developing software it's unlikely that a client can genuinely approve a software requirements specification without some way of understanding what that specification implies about the implemented software. Granted, a well-written specification isn't necessarily hard to understand. What *can* be hard to understand is the full complexity of how the various requirements will combine to define and constrain the software behavior, and what the actual experience of interacting with that software will be like.

But, just like a playing a few notes on a piano can help to bring a score to life, we can bring software requirements to life using prototypes or incremental builds that aren't yet feature-complete. That's sort of the point of the regular demonstrations of working software that are part of many agile software development processes. Beyond just being a useful way of showing the client that you're making progress (and therefore should be paid), the demo is a great way to make the requirements *tangible* and to gather *feedback* about how the software should really behave. That feedback provides the development team with a better understanding of what the client is after, which can inform both revisions to the already-implemented features, and refinements to the requirements for not-yet-implemented functionality.

## Coda

Showing a client working software is a good way to help them (and you) understand their real requirements. Is a working product *always* the best and most cost-effective way to "bring the requirements to life" and gather feedback? I'm not sure.

A working product is often *not* the best way in other engineering disciplines. The cost and time for injection-molding a part or fabbing a printed circuit board is so much greater than the equivalent for software that using a working product to gather feedback may not be feasible (although technologies like 3D printing are changing that equation). Engineers trying to apply an agile approach in non-software disciplines probably need to consider what other things they can do to help their clients understand the requirements. And maybe software engineers should be considering what other things *we* could be doing to make requirements tangible. Are there other ways to bring the requirements to life, and get the answers we need, that are cheaper or more effective than creating working software?

Because ultimately what we're trying to do is understand what the client needs (the requirements), and implement software that meets those needs. The faster, better, and cheaper we can reach that understanding and implement that software, the happier our client will be. And the more likely we are to score an encore project.
