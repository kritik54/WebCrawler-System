# Test Suite

This directory contains sample automated and documentation-based tests for the **Topic-Specific Web Crawler and Search Engine**.

## Structure

* **UnitTests/** – Tests individual modules independently.
* **IntegrationTests/** – Tests communication between modules.
* **PerformanceTests/** – Documents performance and load testing procedures.
* **SecurityTests/** – Documents security testing procedures.

## Running the Tests

From the project root directory:

```bash
python -m unittest discover tests
```

Or run a specific test:

```bash
python tests/UnitTests/test_url_frontier.py
```

This command discovers and executes all unit and integration tests contained in the `tests/` directory.

These tests demonstrate the testing strategy described in the System Design Document and provide a foundation for future implementation.
