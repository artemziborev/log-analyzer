# Log Analyzer

[![CI](https://github.com/USERNAME/log-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/log-analyzer/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/github/license/artemziborev/log-analyzer.svg)](LICENSE)

A CLI-based log analyzer for nginx access logs that parses and aggregates statistics for performance analysis. Built with Clean Architecture, tested with pytest, and ready for CI/CD and Docker deployment.

## 🚀 Features

- Parses nginx access logs (`.log` or `.gz`) with `$request_time`
- Aggregates per-URL metrics:
  - Request count and percentage
  - Total, average, max, and median request times
- Renders an interactive HTML report (sortable table)
- Automatically skips already processed logs
- Configurable via `--config` YAML
- Safe parsing: exits if error threshold exceeded
- Logs errors and progress using `structlog`
- Fully tested, pre-committed, Dockerized, and CI-ready

## 📦 Project Structure

```bash
├── main.py                      # CLI entrypoint
├── config.yaml                  # Example config
├── templates/report.html        # HTML report template
├── logs/                        # Log input directory
├── reports/                     # Output directory for reports
├── src/app/                     # Core logic (Clean Architecture)
│   ├── domain/                  # Interfaces & models
│   ├── services/                # Parser, analyzer, config loader
│   └── presentation/            # HTML renderer
├── tests/                       # Unit tests (pytest)
├── Dockerfile                   # Docker support
├── Makefile                     # Lint/test/run shortcuts
├── .pre-commit-config.yaml      # Linters and type checks
└── .github/workflows/ci.yml     # GitHub Actions CI
```

## ⚙️ Usage

### CLI

```bash
poetry run python main.py --config config.yaml
```

### Config Example (`config.yaml`)

```yaml
log_dir: logs
report_dir: reports
report_template: templates/report.html
report_size: 1000
error_threshold: 0.2
```

### Docker

```bash
docker build -t log-analyzer .
docker run --rm \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/reports:/app/reports \
  -v $(pwd)/templates:/app/templates \
  log-analyzer
```

## ✅ Requirements

- Python 3.12
- Poetry
- `pre-commit`, `black`, `flake8`, `isort`, `mypy`, `pytest`

## 🧪 Testing

```bash
make test
```

## 📈 CI/CD

- GitHub Actions configured in `.github/workflows/ci.yml`
- Linting, type checks and tests run on every push

## 🪄 Pre-commit Setup

```bash
pre-commit install
```

## 📄 License

MIT License — see `LICENSE` file.
