# Copyright   : (c) 2014 Bernie Pope
# License     : BSD-style
# Maintainer  : florbitous@gmail.com

# A convenience Makefile.

#.PHONY: all configure clean install
#all configure clean install:
#	$(MAKE) $@ --directory=lib
#	$(MAKE) $@ --directory=compiler
#	$(MAKE) $@ --directory=readpyc
#
#.PHONY: dev
#dev:
#	cabal-dev install lib/ readpyc/ compiler/

.PHONY: test
test:
	shelltest --color --execdir test/ -- -j1
