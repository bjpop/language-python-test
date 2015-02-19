# Copyright   : (c) 2014 Bernie Pope
# License     : BSD-style
# Maintainer  : florbitous@gmail.com

# A convenience Makefile.

.PHONY: test
test:
	shelltest --color --execdir test/ -- -j1
