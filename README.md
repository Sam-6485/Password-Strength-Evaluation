# Password-Strength-Evaluation
# Password Strength Evaluation

This project demonstrates how to evaluate password strength using macOS Terminal tools.

## Tools Used
- `cracklib-check`
- Python script to score passwords

## Files
- `passwords.txt`: Test passwords
- `score_passwords.py`: Python scoring script
- `Password_Strength_Evaluation_Report.pdf`: Full lab report

## How to Run
```bash
cat passwords.txt | cracklib-check
python3 score_passwords.py
