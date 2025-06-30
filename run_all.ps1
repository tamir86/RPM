# run_all.ps1 — wrapper for full pipeline

Write-Host "1) Validating filenames…"
python validate_filenames.py --folder 02_Models --output 06_Metadata_And_Indexes/filename_validation_report.csv

Write-Host "2) Fixing filenames…"
python fix_filenames.py --report 06_Metadata_And_Indexes/filename_validation_report.csv --folder 02_Models --apply

Write-Host "3) Generating master metadata…"
python generate_master_metadata.py --folder 02_Models --output 06_Metadata_And_Indexes/master_metadata.csv

Write-Host "4) Merging enrichment…"
python merge_metadata.py

Write-Host "5) Exporting Dublin Core…"
python export_dublin_core.py

Write-Host "✅ All steps complete."
