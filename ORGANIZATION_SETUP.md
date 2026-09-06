# DevTechx Labs Organization Setup

Owner checklist. This file becomes public when committed to the public `.github`
repository. It is written for administrators but is not private storage. Keep
credentials and internal decisions elsewhere; remove this checklist after setup
if desired. Removing it later does not erase Git history.

## Organization identity

| Setting | Value |
| --- | --- |
| GitHub organization | `DevTechx-Labs` |
| Display name | DevTechx Labs |
| Description | Building practical software, developer infrastructure, and intelligent automation for modern teams. |
| Website | [devtechxlab.com](https://devtechxlab.com) |
| Avatar | [1024 px avatar](profile/assets/devtechx-avatar.png) |
| Optional location | Add only if the company wishes to publish it |

The public GitHub API returned organization login `DevTechx-Labs`, display name
`DevTechx Labs`, and type `Organization` on 6 September 2026. All three supplied
domains returned HTTP 200 during setup. These checks establish current public
responses; they do not establish control of the account or domains.

## Before publication

- [ ] Confirm that the destination organization is controlled by DevTechx Labs.
- [ ] Create or inspect the public repository named exactly `.github`.
  If it already exists, review and integrate its contents without overwriting history.
- [ ] Keep `profile/README.md` at the repository root's `profile/` directory.
- [ ] Keep issue forms in `.github/ISSUE_TEMPLATE/` and workflows in `.github/workflows/`.
  The leading repository folder name is separate from this nested `.github/` folder.
- [ ] Publish an official contact address in the profile when available.
- [ ] Set a confidential conduct reporting contact and accountable enforcement owner.
- [ ] Enable private vulnerability reporting for applicable public repositories;
  publish a monitored security fallback address and verify its delivery.
- [ ] Identify the initial maintainers and decision owner in `GOVERNANCE.md`.
- [ ] Review the repository rights notice. A general reuse license is intentionally
  not selected. The code of conduct retains its separate CC BY-SA 4.0 license.
- [ ] Review the light and dark profile at desktop, tablet, and mobile widths.
- [ ] Remove this admin checklist from the initial commit if it should not be public.

### Intentional source tasks

Four comments require owner input:

1. `profile/README.md`: official DevTechx Labs contact email.
2. `CODE_OF_CONDUCT.md`: confidential reporting contact and enforcement owner.
3. `SECURITY.md`: official security contact.
4. `GOVERNANCE.md`: initial maintainers and decision owner.

No organization-slug substitution is needed. There are no invented contact
addresses, projects, technology stacks, or social-proof claims. The license notice
is an explicit conservative choice, not a promise that a future software project
will use the same terms.

## Initialize and push a new repository

These commands assume you are inside this prepared `.github` folder, Git is
installed, your commit identity is configured, and GitHub CLI is installed and
authenticated with permission to create a repository in the organization.
Do not use this new-repository sequence if the remote `.github` already exists.

```sh
gh auth status
gh api orgs/DevTechx-Labs --jq '{login, name, type}'
git init -b main
git add .
git diff --cached --check
git diff --cached --stat
git commit -m "Set up DevTechx Labs organization profile and community files"
gh repo create DevTechx-Labs/.github --public --source=. --remote=origin \
  --description "Organization profile and community guidelines for DevTechx Labs."
git push -u origin main
```

If creating the empty public repository through GitHub's website instead, omit
the `gh repo create` command and use the following after the local commit. The
new remote must be empty; do not initialize a separate README there.

```sh
git remote add origin git@github.com:DevTechx-Labs/.github.git
git push -u origin main
```

This alternative requires GitHub SSH authentication. If the remote already exists,
clone it separately, compare its contents with this package, and integrate through
a branch and pull request. Never force-push over existing organization files.

## Configure the organization

- [ ] Set the display name, description, primary website, official email, and avatar.
- [ ] Add a location only if useful and approved for public display.
- [ ] Verify company domains in organization settings where the account supports it.
  DNS access and GitHub's verification flow are required; a website link is not verification.
- [ ] Require two-factor authentication after owners and members have recovery access.
- [ ] Keep organization ownership limited; maintain a second trusted recovery owner if possible.
- [ ] Review member privileges, who can create repositories, and repository visibility controls.
- [ ] Set the lowest useful default repository permission and grant additional access through teams.
- [ ] Keep experiments private by default; publish only when documentation, licensing,
  security reporting, and maintenance expectations are ready.
- [ ] Add rulesets or branch protection for `main`: review before merging,
  prevent force pushes and deletion, and require relevant checks.
  Keep bypass access deliberate and limited.
- [ ] Review Actions permissions and permitted Actions. Retain read-only workflow
  defaults and review dependency updates before merging them.
- [ ] Enable secret scanning and push protection where available.
- [ ] Enable dependency alerts and use Dependabot updates where appropriate.
  This repository includes monthly GitHub Actions update configuration.
- [ ] Use repository-specific private reporting and security policies as products mature.

Feature availability varies by repository visibility, account type, and plan.
Confirm each setting in the current GitHub organization UI.

### Repository appearance and checks

- [ ] Upload `profile/assets/social-preview.png` as this repository's social preview
  under its general settings. This is separate from the organization avatar.
- [ ] Check the public organization Overview and verify the hero and policy links.
- [ ] Open the new-issue chooser in this repository to confirm all three forms appear.
  No default labels or assignees are assumed, and blank issues are disabled.
- [ ] Check one repository without local forms to verify the inherited defaults.
  A repository with its own valid issue configuration overrides the default form set.
- [ ] Run both Actions manually after the first push. Lint runs on Markdown changes;
  local link checks run on changes, and external links run weekly and manually.
- [ ] Do not require these path-filtered documentation checks on unrelated pull requests:
  skipped workflows may leave a required check pending. If you need them required
  on every change, remove path filtering or add an always-running gate first.

These Actions run only in this repository. Community defaults do not copy workflow
files or licenses into other repositories; add appropriate CI and license choices
to each software project.

## Repository topics

For this profile repository, start with `devtechx` and `documentation`. For future
repositories, consider `developer-tools`, `developer-infrastructure`, `automation`,
`software`, `devtools`, and `infrastructure` only when they describe the actual work.
Use `open-source` only after a repository has an appropriate open-source license.
Topics belong to repositories; they are not substitutes for an organization description.

## Pinned repository strategy

Pin up to six strong public repositories in this future order, when they exist:

1. Flagship product or project.
2. Developer infrastructure project.
3. Open-source utility.
4. SDK, API, or tooling project.
5. Examples or templates repository.
6. Community or documentation repository.

Use fewer pins when fewer repositories are ready. Do not invent projects, publish
empty repositories, or fill slots for appearance. Each pin should help a visitor
understand and use the work. An organization owner can select the Public profile
view, choose **Customize pins** (or **pin repositories**), select repositories,
and save. Review pins as projects mature.

## Repository naming

Prefer simple lowercase names with hyphens: `product-name`, `product-sdk`,
`product-cli`, `product-api`, `developer-tool`, or `infrastructure-component`.
These are naming patterns, not proposed projects.

Avoid names such as `devtechx-project-final`, `test123`, `new-repo`,
`final-version`, `project-v2-final`, and unexplained abbreviations.

## Public repository standard

Before making a software repository public, confirm it has:

- A concise description of the problem solved and a website or documentation URL where relevant.
- Accurate topics, a useful README, working examples, and clear setup instructions.
- An explicit license decision, with brand rights kept distinct.
- Contribution and security guidance, plus issue templates suited to the project.
- Meaningful tests, CI appropriate to the project, and honest visible CI status.
- Release/version information and a stated support policy.

## References

- [GitHub organization profiles and pins](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile).
- [Default community health files and precedence](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).
- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
- [Reporting vulnerabilities privately](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately).
- [Contributor Covenant 3.0](https://www.contributor-covenant.org/version/3/0/code_of_conduct/).
