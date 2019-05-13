default:
	@echo Please specify target
	@for t in $$(cat Makefile | grep '^\w' | cut -d: -f1) ; do echo '-' $$t ; done

test:
	mmpdb fragment test_data.smi -o test_data.fragments
	mmpdb index test_data.fragments -o test_data.mmpdb --properties test_data.csv --smallest-transformation-only --symmetric
	mmpdb transform --smiles 'c1cccnc1O' test_data.mmpdb --property MW
