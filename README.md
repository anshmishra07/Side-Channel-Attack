# Side-Channel-Attack
**Side-Channel Attack Demonstration: Timing Attack on Password Verification**


This repository provides an educational demonstration of a side-channel attack, specifically a timing attack. Timing attacks exploit small differences in processing time to infer sensitive information, such as passwords or cryptographic keys.

In this project, a Python implementation illustrates how an attacker can deduce a password by measuring slight variations in response time during verification. The attack targets systems that check passwords character by character, taking longer to process each correct character. By analyzing these timing discrepancies, an attacker can guess the password character by character until the correct value is found.

**Features**
Password Verification Simulation: A basic function to simulate character-by-character password verification with timing discrepancies.
Timing Attack Code: A script to measure timing differences and guess the password incrementally.
Educational Insight: Detailed comments and explanations to illustrate how timing attacks work and why constant-time comparisons are essential for secure systems.
