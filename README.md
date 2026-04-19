# passgen-cli

A lightweight command-line password generator built with Python.

## Features
- Generates cryptographically secure passwords using Python's `secrets` module
- Password strength checking (0-4 scale)
- Copy generated password directly to clipboard
- Configurable length limits via `config.json`
- Saves generated passwords to a local file

## Installation

Clone the repo and install dependencies:

git clone https://github.com/wyayash/passgen-cli.git
cd passgen-cli
pip install zxcvbn pyperclip

## Usage

Generate a 16-character password:
python passgen.py -l 16

Generate and copy to clipboard:
python passgen.py -l 16 -c

## Configuration

Edit `config.json` to change settings:
- `min_length` — minimum allowed password length (default: 8)
- `max_length` — maximum allowed password length (default: 64)
- `min_strength` — minimum strength score required (default: 2)

## Version History
See [CHANGELOG.md](CHANGELOG.md) for full version history.