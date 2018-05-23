---
layout: post
published: true
title: Enqueuing Embedded Events
tags: [testing,tdd,embedded,software,design,event,event-driven,mocks]
---

Most of my software development career has been in the embedded domain, a subset of software development that sometimes feels like it lags industry trends by a decade or more. One area where embedded has definitely lagged is *test-driven development*. [James Grenning](https://wingman-sw.com/) (one of the original signatories of the Agile Manifesto) has been pushing that particular cause for years with mixed success. For the last few years, my former colleague Matt Chernosky has been writing some really useful, practical guides to embedded TDD at [electronvector.com](http://www.electronvector.com). I recently wrote a [guest piece](http://www.electronvector.com/blog/avoiding-mocks-by-enqueuing-events) for Matt's blog discussing an architectural pattern for event-based embedded systems that makes embedded TDD a little easier. The core idea is to use an event queue and dispatching event loop to decouple parts of the system from each other. It's not exactly a novel idea. But it's one that probably isn't as widely used in embedded systems as it should be. You can find the whole post (and links to working source code) at [http://www.electronvector.com/blog/avoiding-mocks-by-enqueuing-events](http://www.electronvector.com/blog/avoiding-mocks-by-enqueuing-events).
