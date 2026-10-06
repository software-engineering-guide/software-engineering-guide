# Workflow

1. Read the relevant guide: [authoring](../docs/contributing/authoring.md),
   [navigation](../docs/contributing/navigation.md),
   [testing](../docs/contributing/testing.md).
2. Make the smallest change that satisfies the request.
3. If the set of chapters changed, update `spec/structure.md` and run `just nav`.
4. Run `just test`. Then `just spell` and `just lint`, which catch what the suite
   does not; CI runs both.
5. Add a one-line entry to `docs/project/changelog.md`.

Git: the pre-commit hook runs the em-dash check, codespell, and the validation
suite. `origin` pushes to three remotes (Codeberg, GitHub, GitLab); a push can
succeed on some and fail on others, so confirm each with `git ls-remote`.

Dependencies: `uv lock --upgrade`, then `just test` and `just spell`.

Size: every file in `docs/contributing/` and `AGENTS/` stays well under 40 KB so
it loads cheaply into an agent's context.
