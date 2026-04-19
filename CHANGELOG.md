# Changelog

## v1.2 — Clipboard Support
- Added -c flag to copy generated password to clipboard
- Integrated pyperclip library

## v1.1 — Strength Checking
- Integrated zxcvbn library
- Added strength score output (0-4 scale)
- Password now rated from Very weak to Very strong

## v1.0 — Initial Release
- Basic password generation using Python secrets module
- CLI with -l flag for custom length
- Saves generated passwords to passwords.txt
- Configurable settings via config.json