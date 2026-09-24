# Pricing Export Job

An automation that extracts pricing data from an Oracle database, exports it to CSV,
consolidates and compresses the results, and emails the generated files to a
designated recipient.

## Overview

This job connects to the Oracle database behind Brasauto's ERP, runs a set of
predefined queries against the stock/pricing tables for several store/price-list
codes, and produces a set of pricing files that are compressed and delivered by
email. It is meant to run unattended (e.g. via Windows Task Scheduler or a
compiled executable), once per scheduled run.

## Workflow

```text
Oracle Database
      ↓
Data extraction (per price list: 4091, 4091p, 5098, Haipu)
      ↓
CSV generation
      ↓
CSV consolidation (Haipu + 5098 merged into 5098p)
      ↓
Individual ZIP compression (4091, 4091p, 5098, 5098p)
      ↓
Email delivery (all ZIP files attached to one message)
```

## Features

- Oracle database connectivity via `oracledb` (thick mode, using the Instant Client)
- CSV export for four price lists: `4091`, `4091p`, `5098`, and `Haipu`
- Consolidation of the Haipu and 5098 exports into a combined `5098p` file
- Individual ZIP compression of each generated CSV
- Email delivery of all generated ZIP files, with retry on transient SMTP failures
- Path resolution that works both as a plain script and as a PyInstaller-frozen executable

## Project Structure

```text
price-export-job/
├── pricing_pipeline.py      # Entry point — orchestrates the full run
├── pricing_pipeline.spec    # PyInstaller build spec
├── paths.py                 # Project-root and .env-relative path resolution
├── oracle_client.py         # Oracle client initialization and DB connection
├── csv_export_4091.py       # Extracts and exports the 4091 price list
├── csv_export_4091p.py      # Extracts and exports the 4091p price list
├── csv_export_5098.py       # Extracts and exports the 5098 price list
├── csv_export_haipu.py      # Extracts and exports the Haipu price list
├── csv_merger.py            # Consolidates the Haipu and 5098 exports
├── file_compressor.py       # Compresses each exported CSV into its own ZIP
├── email_sender.py          # Attaches and sends the generated ZIP files by email
├── queries/                 # SQL queries, one per price list
│   ├── 4091.sql
│   ├── 4091p.sql
│   ├── 5098.sql
│   └── haipu.sql
└── .gitignore
```

Each `csv_export_*` module follows the same pattern: read its SQL file from
`queries/`, run it against the open Oracle connection, and write the result to a
semicolon-separated CSV (no header row) under the `Ars/<price-list-code>/` folder.

## Requirements

- Python 3 (built and tested with CPython 3.12; no version-specific syntax is used)
- Python packages: `oracledb`, `pandas`, `python-dotenv`
- Oracle Instant Client (thick-mode client libraries; expected under
  `instantclient_23_0/` by default — see Configuration)
- Network access to the Oracle host (Brasauto network/VPN)
- An SMTP account capable of sending mail with attachments

## Configuration

Configuration is read from environment variables, typically supplied via a
`.env` file in the project root (see `.gitignore` — `.env` is intentionally not
committed).

**Oracle connection** (`oracle_client.py`):

```text
ORACLE_LIB_DIR      # Path to the Instant Client libraries (default: instantclient_23_0)
ORACLE_USER
ORACLE_PASSWORD
ORACLE_HOST
ORACLE_PORT
ORACLE_SERVICE
```

**File paths** (`paths.py`, consumed by the export/merge/compress/email modules):

```text
PATH_ARS_BASE         # Base folder for exported CSVs (default: Ars)
PATH_ZIP_OUTPUT        # Folder for the compressed output (default: Output)
```

Relative values are resolved against the project root (or the executable's
folder, when frozen with PyInstaller); absolute values are used as-is.

**Email delivery** (`email_sender.py`):

```text
SMTP_SERVER
SMTP_PORT              # Defaults to 465 (SMTP over SSL)
SMTP_USER
SMTP_PASSWORD
EMAIL_TO
```

No credentials are included in this repository — populate your own `.env` file.

## Usage

```bash
python pricing_pipeline.py
```

A PyInstaller build is also available via `pricing_pipeline.spec`, producing a
standalone executable (see Maintenance Notes below for an important detail
about its current output filename).

## Processing Flow

1. Initialize the Oracle client and open the database connection (`oracle_client.py`).
2. Run each price-list query and export its results to CSV (`csv_export_4091.py`,
   `csv_export_4091p.py`, `csv_export_5098.py`, `csv_export_haipu.py`).
3. Consolidate the Haipu and 5098 CSVs into a combined `5098p` file (`csv_merger.py`).
4. Compress each of the four output CSVs (`4091`, `4091p`, `5098`, `5098p`) into
   its own ZIP archive (`file_compressor.py`).
5. Walk the ZIP output folder, attach every `.zip` found, and send a single email
   to the configured recipient, retrying up to three times on transient SMTP
   errors (`email_sender.py`).

## Error Handling

Each export module catches exceptions around its Oracle query/CSV write and
prints an error rather than raising, so one failing price list doesn't crash the
whole run outright — though `pricing_pipeline.py` does not currently check the
return value of each export step before moving on. `email_sender.py` retries the
SMTP send up to three times (15-second wait between attempts) for transient
server errors. Oracle client initialization and connection failures in
`oracle_client.py` are fatal and exit the process immediately, since nothing
downstream can run without a database connection.

## Logging

There is no structured logging; all status and error output goes to stdout via
`print()`. When run unattended, stdout should be redirected to a file if a
record of each run is needed.

## Maintenance Notes

- **Executable name mismatch (intentional, needs follow-up):** the entry script
  was renamed from `mestre.py` to `pricing_pipeline.py`, and `pricing_pipeline.spec`
  was updated to build from it. The build's output executable name was
  deliberately **left as `mestre`** (`dist/mestre.exe`) so this rename doesn't
  silently break an external Windows Task Scheduler job or `.bat` file that may
  already point at `mestre.exe`. If/when you update that scheduled task, you can
  rename the `name=` field in `pricing_pipeline.spec` to `pricing_pipeline` and
  rebuild.
- On-disk folder names (`Ars`, `Output`, and the per-price-list
  subfolders like `PFO4091`) were intentionally left unchanged, since they are
  the actual paths the job reads from and writes to.
- The four `csv_export_*` modules are near-duplicates of each other (same
  structure, different price-list code and SQL file). This is a pre-existing
  pattern in the codebase, not something introduced by this pass — no
  consolidation was made, since this task is limited to renaming and
  documentation, not refactoring.

## License

No license file is currently included in this repository.
