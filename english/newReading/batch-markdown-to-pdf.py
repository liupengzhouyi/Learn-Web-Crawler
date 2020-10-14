from pathlib import Path
import os

work_dir = Path.cwd()

export_pdf_dir = work_dir / 'word'
if not export_pdf_dir.exists():
    export_pdf_dir.mkdir()

for md_file in list(work_dir.glob('*.md')):
    md_file_name = md_file.name
    pdf_file_name = md_file_name.replace('.md', '.docx')
    pdf_file = export_pdf_dir / pdf_file_name
    # pandoc --word-engine=xelatex test.md -o test.word
    cmd = "pandoc '{}' -o '{}'".format(md_file, pdf_file)
    os.system(cmd)