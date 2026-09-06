# Contributing to DevTechx Labs

Focused improvements are welcome. Each project's own contribution guide takes
precedence where it sets more specific requirements. Please follow our
[code of conduct](CODE_OF_CONDUCT.md).

## Before opening an issue

Read the project documentation, check its supported versions, and search existing
issues and pull requests. Keep one problem per issue. Remove credentials, personal
data, customer information, and private URLs from examples and screenshots.

For suspected vulnerabilities, follow [SECURITY.md](SECURITY.md). Do not post
exploit details in a public issue or pull request.

## Reporting bugs

Use the bug report form in the affected repository. Include a minimal reproduction,
the version or commit, your environment, expected and actual behavior, and relevant
sanitized logs. If you cannot reproduce the issue consistently, describe what you
observed and what you have already tried.

## Suggesting features

Explain the problem, who encounters it, and what a useful outcome would look like.
Include your proposed solution and alternatives. Discuss substantial changes before
investing in a large implementation; an open request does not imply a delivery commitment.

## Pull request workflow

1. Fork the relevant repository, or use a branch if you have access.
2. Start from its default branch. Use a short name such as `fix/link-target`,
   `feat/export-option`, or `docs/setup-guide`.
3. Keep the change focused. Follow the surrounding conventions and avoid unrelated formatting.
4. Run the checks appropriate to the change and review your own diff for secrets and accidental files.
5. Open a pull request explaining what changed, why, and how you verified it.
   Link the relevant issue when one exists and call out compatibility changes.
6. Respond to review, update the branch as needed, and let a maintainer merge it.

Use concise, descriptive commit subjects, such as `Fix relative asset links`.
Conventional Commits are welcome when a project uses them, but are not a requirement
of this community repository. No contributor agreement or sign-off is implied here.

## Testing and documentation

Add regression coverage for behavior changes where the project supports it.
For documentation or brand updates, check links, Markdown, image dimensions, alt
text, and rendering at desktop and mobile widths in light and dark themes.
Explain checks you could not run rather than claiming they passed.

Update setup instructions, examples, and release notes when behavior changes.
For this repository, the lint workflow checks Markdown and the link workflow checks
references. After changing the approved artwork, use the [asset guide](ASSETS.md)
to regenerate derivatives and inspect them before committing.

## Review and scope

Maintainers review correctness, clarity, compatibility, maintenance cost, and fit
with the project's direction. They may request a smaller change or decline a proposal.
There is no fixed review timeline. Contributions do not automatically confer
maintainer access. See [GOVERNANCE.md](GOVERNANCE.md) for decision ownership.

Check the destination repository's license before contributing. This repository's
[rights notice](LICENSE) does not grant a general reuse license for its original
content or brand assets.
