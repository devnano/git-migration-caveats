# Git & Django Migration Caveats

A demonstration repository showcasing common pitfalls with Git workflows and Django migrations.

## Caveat 1: Cherry-Pick and GitHub PR Diffs

GitHub uses a **three-dot diff** (`base...head`) for PR comparisons. This shows all changes since the merge-base (common ancestor) of the two branches.

### The Problem

When you cherry-pick commits:
- Git creates a new commit with a **different SHA**, even if the content is identical
- GitHub sees the original and cherry-picked commits as completely different
- GitHub's diff algorithm compares **commit ancestry**, not content
- Result: "phantom" changes appear in PR diffs

### Example Scenario

```
main:       A -- B -- C -- D
             \
staging:      B' -- C'  (cherry-picked B and C)
```

When opening a PR from `main` to `staging`:
- The merge-base might be before B
- GitHub shows B, C, D as changes
- Even though B' and C' have identical content to B and C, they have different SHAs
- The diff shows changes that are already in staging

### Demo Structure

This repo demonstrates this with:
- `main` branch: sequential feature commits
- `staging` branch: cherry-picked commits from main
- PRs showing the "phantom diff" phenomenon

### Workarounds

1. **Periodic merge syncs**: Merge staging back into main occasionally
2. **Merge-based workflow**: Have feature branches merge into all targets
3. **Accept the noise**: Review commit list rather than diff
4. **Squash before cherry-picking**: Reduces but doesn't eliminate noise

### Why GitHub Won't Fix This

This isn't a bug - it's a fundamental consequence of how Git tracks history by commit identity (SHA) rather than content.

---

## Live Demo

**PR #1**: [Cherry-Pick Phantom Diff Issue](https://github.com/devnano/git-migration-caveats/pull/1)

### Evidence

| Source | Files in Diff |
|--------|---------------|
| GitHub PR | 3 files (feature_a, feature_b, feature_c) |
| `git diff staging main` | 1 file (feature_c only) |

### Commit SHAs (proof of different identities)

| Feature | main | staging | Content Identical? |
|---------|------|---------|-------------------|
| Feature A | `229448b` | `ae262a8` | Yes |
| Feature B | `ff62546` | `5e3b672` | Yes |
| Feature C | `99a9bf2` | N/A | Only on main |

---

## Branches

- `main`: Primary development branch
- `staging`: Receives cherry-picked commits for staged releases

