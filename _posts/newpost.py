#!/usr/bin/python

# Derived from Bruce Eckel's NewPost.bat, https://github.com/BruceEckel/BruceEckel.github.io/blob/master/_posts/NewPost.bat

import os, string, datetime, sys, subprocess

def main(argv):
  name = argv[0]
  postname = name.lower().strip().replace(" ", "-")
  postname = datetime.date.today().strftime("%Y-%m-%d-") + postname + ".md"

  slugline = """---
layout: post
published: false
title: %s
tags: []
---

""" % string.capwords(name)

  with open(postname, 'w') as f:
      f.write(slugline)

# Not using this right now
#  subprocess.call(["atom", postname]) 


if __name__ == "__main__":
   main(sys.argv[1:])
