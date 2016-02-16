PYSRC=$(shell ls git_stats/*.py)

test:
	nosetests git_stats 

quality: pylint flake8

flake8:
	flake8 $(PYSRC)

pylint:
	-pylint -f parseable $(PYSRC)
