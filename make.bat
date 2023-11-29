@echo on
sphinx-apidoc -f -T -M -E -o docs/source poetex *test*
cd /d "docs"
make clean && make html && cd /d ..
