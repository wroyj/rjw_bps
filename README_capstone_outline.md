# RJW Data Entry & Backup System Capstone Project

## ✅ Project Vision and Purpose
This project is designed as the capstone for Roy J Wheelock's data science portfolio.  
The system will serve as:

- A configurable data entry module for various projects (medical logs, garden data, lab notes, etc.)
- A bulletproof backup system with automated audit trails and recovery functionality.
- A flexible, template-based system for future projects without starting from scratch.
- An example of **literate programming** combining code and clear documentation.
- The basis for a research paper detailing design, implementation, and applications.
- A platform for showcasing work online (via GitHub, Docker, and a future portfolio website).

## ✅ Core Components Built So Far

| Component                    | Purpose                                                                          |
|------------------------------|----------------------------------------------------------------------------------|
| **Directory structure**       | Standard `data/input`, `data/backup`, `data/staging`, `logs`, and audit trail.  |
| **Config system (config.sh)** | Easily tailor each new project with names, paths, and file structures.           |
| **Setup script**             | Creates directories and assigns correct permissions.                             |
| **Backup system**            | Uses `rsync` and JSON audit logging to save session data and input files.       |
| **Recovery script**          | Allows restoring backups by timestamp or the most recent session.                |
| **Makefile**                 | Provides one-line commands like `make setup`, `make backup`, `make export`.     |
| **Jupyter notebook scaffold**| For interactive development and testing of data entry workflows.                 |
| **Manual export workflow**   | Converts `.ipynb` to `.py` and stores in `data/input/session_code/` for backup. |
| **Full Dockerfile**          | Containerizes development environment for reproducibility.                       |
| **docker-compose.yml**       | Enables single-command startup of the entire system with Jupyter Lab.           |

## ✅ Unique Features

- Built with **Knuth's literate programming** philosophy.
- Designed as a **configurable template system** for long-term reuse.
- Includes a research paper as a deliverable, documenting all design decisions and applications.

## ✅ Deliverables Created So Far

- ✔️ Project config tools and templates (in `data_entry_rjw_bps/`)
- ✔️ Jupyter notebook starter (`bp_data_entry.ipynb`)
- ✔️ Full Dockerfile and `docker-compose.yml` setup
- ✔️ Research paper outline in LaTeX (`research_paper_outline.tex`)
- ✔️ Starter bibliography (`references.bib`)

## ✅ Next Steps

- Fully develop `backup.sh` and `recover.sh` production-level scripts.
- Write the research paper, filling each section.
- Set up GitHub version control and publish the repository.
- Build a personal portfolio website (possibly using GitHub Pages).
- Create a README-cheatsheet and live examples.

---

> *This README file is generated as part of the ongoing literate programming process.*
