# Security Test Plan

## Objective

Verify resistance to common web application attacks.

## Test Cases

| Test                              | Expected Result                        |
| --------------------------------- | -------------------------------------- |
| SQL Injection                     | Blocked                                |
| Cross-Site Scripting (XSS)        | Rejected                               |
| Cross-Site Request Forgery (CSRF) | Denied                                 |
| Invalid Login Attempts            | Account locked after repeated failures |
| Unauthorized Access               | Access denied                          |

## Tools

* OWASP ZAP
* Browser developer tools
* Manual penetration testing

## Expected Result

All security controls operate correctly and prevent unauthorized access.
