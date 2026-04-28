# Security Policy

## Supported Versions

We support security fixes on the latest release only.

| Version | Supported |
| ------- | --------- |
| latest  | ✅        |
| older   | ❌        |

## Reporting a Vulnerability

If you discover a security vulnerability, **please do not open a public issue**.

Instead, report it privately by emailing the maintainers or using
[GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).

We will acknowledge your report within 72 hours and aim to issue a fix within 14 days.

## Security Best Practices for Users

- Never commit API keys or secrets to the repository.
- Use environment variables (e.g., `BAILIAN_API_KEY`) to supply credentials at runtime.
- Review dependencies regularly with `pip audit` or similar tools.
