###
### Example)
###   $ NUM=000004 make prep
###   $ NUM=000004 make test
###   $ NUM=000004 make clean
###

default:
	@echo Please specify target
	@for t in $$(cat Makefile | grep '^\w' | cut -d: -f1) ; do echo '-' $$t ; done

# NUM = '000004'

prep:
	python make_data.py $(NUM)_orig.smi

test:
	mmpdb fragment $(NUM).smi -o $(NUM).fragments
	mmpdb index $(NUM).fragments -o $(NUM).mmpdb --properties $(NUM).csv --max-radius 3
	mmpdb transform --smiles 'c1cccnc1O' $(NUM).mmpdb --property logP
	python inspect_mmpdb.py $(NUM).mmpdb

clean:
	@rm -rf *~ *.bak
	@rm -rf __pycache__
	rm -rf $(NUM).csv $(NUM).fragments $(NUM).mmpdb $(NUM)_mmpdb.csv $(NUM).smi
