# poetex
Convert text files into tex files.

# Regenerate documentation

`
sphinx-apidoc [options] -o <outputdir> <sourcedir> [pathnames ...]
`

or, more specifically:

`
sphinx-apidoc -f -T -M -E -o docs/source poetex *test*
`
`
cd docs && make html && cd .. 
`
`
cd docs && make clean cd .. 
`

# Contributing

1. Install poetry
2. Install dependencies
3. Install pre-commit
4. Install pre-commit message
5. Rebuild docs
