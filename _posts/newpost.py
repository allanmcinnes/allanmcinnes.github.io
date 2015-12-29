#!/usr/local/bin/python3

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
---

""" % string.capwords(name)

  with open(postname, 'w') as f:
      f.write(slugline)

  subprocess.call(["sublime", postname]) 


if __name__ == "__main__":
   main(sys.argv[1:])