include config.sh

backup:
	 ./backup.sh

recover:
	 ./recover.sh

recover-timestamp:
	@echo "Enter timestamp to recover:"
	read ts && sudo ./recover.sh $$ts

export:
	@mkdir -p data/input/session_code
	jupyter nbconvert --to script bp_data_entry.ipynb --output-dir=data/input/session_code

setup:
	 ./setup_backup_directories.sh
