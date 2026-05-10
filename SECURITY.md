# Security Policy

## Supported Versions

The following versions of this project are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |
| < 1.0   | :x:                |

---

## Reporting a Vulnerability

We take the security of this project seriously. If you discover a security vulnerability, please follow the responsible disclosure process outlined below.

**Do NOT open a public GitHub issue for security vulnerabilities.**

### How to Report

1. **Email:** Send a detailed report to the repository owner via GitHub's private contact options or through the email associated with this account.
2. **Include the following in your report:**
   - A clear description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact and severity assessment
   - Any suggested mitigations or fixes
   - Your contact information (optional, for follow-up)

### Response Timeline

| Action                          | Timeframe         |
| ------------------------------- | ----------------- |
| Initial acknowledgment          | Within 48 hours   |
| Vulnerability confirmation      | Within 7 days     |
| Patch or mitigation released    | Within 30 days    |
| Public disclosure (coordinated) | After patch ships |

We are committed to working with reporters to understand and resolve issues quickly. We will keep you informed throughout the process.

---

## Disclosure Policy

- Security issues will be handled under a **coordinated disclosure** model.
- We ask that you give us a reasonable amount of time (up to 90 days) to remediate a vulnerability before public disclosure.
- We will credit reporters in the release notes unless anonymity is requested.
- We will not pursue legal action against researchers who act in good faith and adhere to this policy.

---

## API Key Handling

This application uses external API keys (e.g., OpenWeatherMap API). The following rules **must** be followed at all times:

### Rules for Contributors

- **Never commit API keys, tokens, or secrets** to the repository — not even in comments, test files, or commit messages.
- API keys must be stored in environment variables or a `.env` file that is listed in `.gitignore`.
- A `.env.example` file with placeholder values (e.g., `WEATHER_API_KEY=your_api_key_here`) should be used instead.
- Rotate any key that has been accidentally exposed immediately and revoke the old one.
- Do not hardcode fallback or default keys in source code.

### Recommended `.env` Setup

```
# .env.example — Copy to .env and fill in your values. Never commit .env.
WEATHER_API_KEY=your_api_key_here
```

### If a Key Is Accidentally Exposed

1. **Immediately revoke** the exposed key from the provider's dashboard.
2. **Generate a new key** and update your local `.env`.
3. **Remove the key from git history** using `git filter-repo` or BFG Repo Cleaner.
4. Notify the repository maintainer so the commit history can be audited.

---

## Secure Development Guidelines

All contributors are expected to follow these practices:

### General Practices

- Keep all dependencies up to date; run `npm audit` regularly and resolve high/critical findings.
- Never disable security linting rules without documented justification.
- Validate and sanitize all user inputs before processing or displaying them.
- Avoid using `eval()`, `innerHTML` with user-controlled content, or other XSS-prone patterns.

### Environment & Configuration

- Use `.env` files for all sensitive configuration; never use hardcoded values in code.
- Ensure `.env` is included in `.gitignore` before your first commit.
- Prefer environment-specific configurations (development, staging, production).

### Dependency Management

- Pin dependency versions in `package.json` to avoid unintended upgrades.
- Review changelogs before upgrading packages, especially major versions.
- Remove unused dependencies promptly.

### Code Review

- All changes must go through a pull request review before merging to `main`.
- Security-sensitive changes (authentication, API calls, data handling) require extra scrutiny.
- Do not merge PRs with unresolved security warnings from automated scans.

### Secrets Scanning

- Enable GitHub's **Secret Scanning** and **Push Protection** features in repository settings.
- Consider adding a pre-commit hook (e.g., `git-secrets` or `detect-secrets`) to catch leaks before they reach the remote.

---

## Security-Related Resources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)
- [npm audit documentation](https://docs.npmjs.com/cli/v10/commands/npm-audit)
- [OpenWeatherMap API Security](https://openweathermap.org/appid)

---

*This security policy was last updated: May 2026.*
