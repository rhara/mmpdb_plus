default:
	@echo Please specify target
	@for t in $$(cat Makefile | grep '^\w' | cut -d: -f1) ; do echo '-' $$t ; done

test_data:
	mmpdb fragment test_data.smi -o test_data.fragments
	mmpdb index test_data.fragments -o test_data.mmpdb --properties test_data.csv --smallest-transformation-only --symmetric
	mmpdb transform --smiles 'c1cccnc1O' test_data.mmpdb --property MW

test_000064:
	mmpdb fragment 000064.smi -o 000064.fragments
	mmpdb index 000064.fragments -o 000064.mmpdb --properties 000064.csv --smallest-transformation-only --symmetric
	mmpdb transform --smiles 'c1cccnc1O' 000064.mmpdb --property logP

make_data:
	python make_data.py 000004_orig.smi

test_000004:
	mmpdb fragment 000004.smi -o 000004.fragments
	mmpdb index 000004.fragments -o 000004.mmpdb --properties 000004.csv --max-radius 3
	mmpdb transform --smiles 'c1cccnc1O' 000004.mmpdb --property logP
	python inspect.py 000004.mmpdb
