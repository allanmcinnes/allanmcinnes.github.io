---
layout: post
published: true
title: Reflecting on Retrospectives
---

I'm coming to believe that frequent *retrospectives* may be one of the most important
practices to incorporate into the team software development process. Maybe
that isn't too surprising, since this blog is partly inspired by Sch&ouml;n's
work on "reflection-in-action". A retrospective is essentially "reflection-in-action"
for project teams. And it has the same kind of value for a team that individual
"reflection-in-action" has: the evaluation of actions and their effects can
help you to get better at what you're trying to do.

## Looking back

The classic retrospective, as described by Norm Kerth in [*"The Ritual of Retrospectives"*](http://clearspecs.com/joomla15/downloads/ClearSpecs62V01_The%20Ritual%20of%20Retrospectives_Kerth.pdf) (*Software Testing & Quality Engineering Magazine*, September/October 2000), occurs at the end of a project.
It involves having the team assess, in a non-judgmental way, how the project went and what lessons
can be learned from it. But that kind of retrospective is a major event -- Kerth recommends taking
a day or two for the retrospective -- and it can only have an impact on the *next* project, not the current one.

## Anything worth doing is worth overdoing

While I don't doubt the value of end-of-project retrospectives, I think there's even
more value to be had by holding frequent retrospectives while the project is actually underway.
Holding frequent retrospectives provides your team with rapid feedback on the development
process, and allows the team to fine-tune the way they're working.

Because you're not waiting until the end of the
project the retrospective session can be much shorter (ours typically run for 1-2 hours instead of 1-2 days).
And the lessons you gather can have an immediate impact on your current project:  
> - Not doing enough pair-programming?
> - Finding that
too many people are checking in broken code?
> - Think that the new test framework is really helpful and should
be used more? 

These things will all come up during a retrospective. Bad practices
are discouraged. Good practices are encouraged. And new practices are introduced to resolve perceived problems.

Having frequent retrospectives is particularly easy to accomplish if you're using a Scrum-like approach with a regular cadence of sprints. But I think it's worth doing regardless of what kind of development
cycle you're using. Not only can it help fine-tune your process, but the chance to
reflect on recent successes can help to improve team cohesion.

## Retrospection in action

Hopefully by this point I've convinced you that you should be holding frequent retrospectives. But
what does that actually involve? Well, for starters, I absolutely encourage you to read Kerth's [*"The Ritual of Retrospectives"*](http://clearspecs.com/joomla15/downloads/ClearSpecs62V01_The%20Ritual%20of%20Retrospectives_Kerth.pdf) for an excellent overview of how to run a retrospective session (although I'll note that we typically find value in something less formal and more lightweight than what he describes). Beyond that, there are a lot of [different ways](http://retrospectivewiki.org/index.php?title=Retrospective_Plans) to approach the actual gathering of information in a retrospective. I certainly haven't tried
them all. With that said, here's what's been working well on the teams I've been involved with recently.

### Some simple questions
The questions we're currently asking are:

 - *What went well?*
 - *What didn't go well?*
 - *What can we do better next time?*

The first question is important as a chance both to reinforce good practices, and to celebrate the team's most
recent victories. It helps prevent the retrospective from becoming overwhelmingly negative.

The second and third questions identify
problems and look for solutions. I've seen teams spontaneously decide that they need
to have stand-up meetings, that more pair sessions would be helpful, that fewer meetings would be better for everyone,
or that the testers need to be involved in the project now rather than later. It's these small adjustments in
the way the team operates that improve the team's performance sprint after sprint.

### Round and round we go

To give the proceedings a little structure, and make sure everyone gets a chance to speak, we typically gather answers to the
*"What went well?"* and *"What didn't go well?"* questions in a round-robin. Anyone can "pass", but no one gets skipped. When everyone is saying "pass", we move to the next question.

The final question is treated in a much more free-form manner, befitting its creative nature. Anyone is free to call out suggestions. The end result is usually a list of 3 or 4 things to implement or change in the following sprint.

This process may sound a little rigid. But the actual meetings tend to be fairly informal, and in fact can be a lot of fun (especially when the most common answer in the first retrospective to *"What can we do better next time?"*  is *"Have beer at the retrospectives"*).

## TL;DR

Frequent retrospectives are perhaps the most important practice to include in the software development process, because they
facilitate having other valuable practices be introduced on an as-needed basis to fine-tune the project. By regularly asking *"What went well?"* and *"What can we do better?"* teams can get the internal feedback they need to rapidly improve their performance. And they can have fun doing it.
