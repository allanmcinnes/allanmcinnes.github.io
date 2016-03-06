---
layout: post
published: false
title: Writing Software Functional Requirements
---
I've been thinking a lot about software requirements lately. Not the most exciting topic, I know. But they're something I seem to struggle with on a daily basis, and I've seen plenty of other people struggle with them too. Yet they're incredibly important for software development. Having a good set of requirements makes design and implementation *so much* easier. Even if you're following an agile approach, reaching a clear definition of *done* for a user story makes it much easier to know what you're supposed to implement. So why are they so hard to get right?

## "The system shall..."

I suspect that part of the problem is that the traditional *"shall statement"* style of requirements were originally developed to write specifications for systems with limited behavior. They work well for describing *properties* a system must have (e.g., *"The system shall mass no more than 50kg"*, or *"The output gain at frequencies below 100Hz shall be at least 20dB"*). But, because they  describe timeless truths about a system rather than dynamic changes, requirements structured that way are not very good for describing behavior (which is, after all, what software is largely about). And yet it's not uncommon to see software functional requirements that look like this:

> The system shall allow the user to create, edit, and delete calendar entries.

This is really just a definition of a property the system must have, rather than a behavior it must exhibit. User story acceptance criteria often have the same problem (converting the requirements statement above into a typical checklist-style list of acceptance criteria for a user story is left as an exercise for the reader). Requirements like this are useful in the sense that you can check off whether or not the software has all of the specified properties, but they don't really say what the software *must do*. Why do we use requirements like that? Because that's how requirements documents have traditionally been written, that's why.

Just as bad are requirements that go too far the other way, and tightly prescribe internal software control flow:

> The system shall allow the user to choose an entry to copy to a new date, and then:
 1. Shall iterate through the list of calendar entries until the selected entry is found
 2. Shall create a new entry with the specified date at the end of the list
 3. Shall copy the information from the selected entry to the new entry

On the positive side, this does at least specify some kind of behavior. But it's the wrong kind of behavior, since it's all about internal operations. It isn't a requirement, it's a description of a design. I mean, ok, it does use the word "shall". But that doesn't automatically make it a requirement. How can you tell it's not really a requirement? Because it's essentially impossible to verify without using a debugger to step through the code. If you can't observe it during a test, then the user or customer probably doesn't care about it (ok, yes, there are some situations in which a customer will require that you use a specific algorithm to do something, but those are the exception rather than the rule).

## Back to basics

I claim that properties don't make good functional requirements. Neither do detailed algorithm specifications. So what *am* I suggesting a software functional requirement should look like? That's the question I've been pondering on and off for the last couple of months. And where that pondering has taken me is back to the basics. So, let's look at those basics.

1. Requirements should specify *what* a system should do, but not *how* it does it. In other words, it should treat the system as a black box. There may be many possible designs that could fit into that black box and meet the requirements. But the end-user doesn't care what's in the box, they just care about what the box does for them.

2. The *what* that software does is to produce behavior (i.e., sequences of things that happen). If we’re approaching the software as a black box the only way we can describe its behavior is in terms of observable phenomena at the interfaces to the black box: inputs and outputs. These are not new thoughts. Michael Jackson's seminal ["The World and the Machine"](http://users.mct.open.ac.uk/mj665/icse17kn.pdf) talks about specifying software behavior in terms of "shared phenomena" at the interface between the system and its environment. Wymore’s [Model-Based Systems Engineering](https://www.crcpress.com/Model-Based-Systems-Engineering/Wymore/9780849380129) describes system functional requirements in terms of input/output sequences, as does [Cleanroom Software Engineering](http://www.drdobbs.com/architecture-and-design/cleanroom-software-engineering/184405405). Like I said, we're going "back to basics" here.

So, a software functional requirement should say something about the required sequences of inputs and outputs (where inputs may come not just from the user but from hardware, and outputs may go to things like databases or network interfaces). Since most of the software we tend write is *reactive* (outputs occur in response to triggering inputs), we should expect most functional requirements to describe a required relationship between a triggering input and the corresponding output: *"when &lt;some event occurs&gt;, then &lt;some output is produced&gt;"*.

Again, this isn't exactly a new thought. Software requirements guru Karl Wiegers [recommends](http://www.jamasoftware.com/wp-content/uploads/documents/wiegers-writing-high-quality-requirements.pdf) phrasing requirements in the form  *"When Y happens, the system shall do X."*, which is pretty much the form I just mentioned above.

## It's a given

We're not quite done though. Sometimes the output we should get depends on more than just the current triggering event. It also depends on what has happened in the past. Which output we get is determined by an entire sequence of inputs, instead of just the current input (this is basically just a complicated way of saying "software is a state machine", but that's a topic for separate note).

One way to deal with this is to write out requirements in terms of sequences of inputs and their corresponding sequences of outputs. But the resulting set of requirements is unlikely to be all that useful to software developers trying to implement something that meets the requirements.

A better way to deal with the problem of history-dependence is to summarize that past history in terms of a *state* that the system must be in before a triggering event produces a particular required output. This is the *Given* in the classic *Given/When/Then* scenario structure popularized by Dan North for [Behavior-Driven Development](http://dannorth.net/introducing-bdd/). I guess it shouldn't be much of a surprise that something called "Behavior-Driven Development" incorporates a good way to describe behavior.

## What's required

Yes, that's right. All that pondering I've been doing led me to the *Given/When/Then* from BDD. That's what I think most software functional requirements should look like. Well, provided the *Given* says something about the observable past history of the system, and that the *When* and *Then* refer to observable inputs and outputs.

> - *Given* some stuff happened in the past
> - *When* some event occurs
> - *Then* the system does something

Looking at this framework, we can see what's wrong with a property-style requirement masquerading as a functional requirement: it leaves out the *Given* and the *When*. And, in some ways, even the *Then*. In fact, it's not really clear what behavior it's specifying. Returning to the original example, presumably users should not *always* be able to edit calendar entries. Instead, we should see something more like (I do not claim that this is a perfect requirement):

> - *Given* the number of calendar entries created is greater than the number that have been deleted
> - *When* the user chooses to edit a calendar entry
> - *Then* an editable version of the current entry content is displayed

(Note: I don't claim that this is a perfect requirement--writing requirements isn't easy and this could probably stand some refinement--but I think it's clearer about the required behavior than the original version)

That's not to say that property-style requirements aren't useful too. Some things really are "timeless truths" for a particular piece of software (e.g., *"The lines on the graph shall be blue"*). But most software requirements should define behavior, and the *Given/When/Then* structure is a good way to define behavior.

Furthermore, because we're restricting the *Given/When/Then* to refer only to observable phenomena we don't end up with a requirement like the second example, in which a debugger is needed for verification. Instead, we have a requirement that:

1. Probably describes what the user will actually see and care about, instead of over-constraining the design,
2. Is actually *testable*. Which is one of the holy grails of requirements-writing.

## TL;DR

So, to recap:

* Write software functional requirements (or user story acceptance criteria) in terms of **observable phenomena** at the interfaces to the software (i.e., inputs and outputs).

* Use a **Given/When/Then** structure to define the required behavior as a relationship between past history, present input, and expected output.

I've been experimenting with this approach lately. I've found it to be helpful for getting me to focus on the *requirements* (rather than the design), and for producing clear, testable requirements statements. Maybe you'll find it helpful too.

## Threads haven't followed (yet)

This is obviously a large topic, and I've only skimmed the surface here. In no particular order, here are a few topics that branch off from the current discussion, but which I chose not to pursue here:

* The difference between a property-style requirement (which expresses what I've called a "timeless truth") and a behavioral requirement (which says something about *when* something should happen) is something like the difference between classical Boolean logic and [temporal logics](https://en.wikipedia.org/wiki/Temporal_logic).

* A *Given/When/Then* structure essentially specifies a state transition. The *Given* describes the starting state, the *When* defines the transitional event, and the *Then* describes the end state.

* Many of the formalisms for specifying what software should do (e.g., Z, the B-Method, TLA+, SCR, or CSP) are structured mathematical way of expressing state transitions.

* What about "non-functional" requirements? I haven't really touched on them at all here.
