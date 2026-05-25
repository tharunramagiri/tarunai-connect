# tarunAI Connect Skills

This directory is the canonical `npx skills` surface for in-repo tarunAI Connect
harnesses.

Layout:

```text
skills/
  tarunai-connect-audacity/SKILL.md
  tarunai-connect-blender/SKILL.md
  ...
```

Typical usage:

```bash
npx skills add tharunramagiri/tarunai-connect --list
npx skills add tharunramagiri/tarunai-connect --skill tarunai-connect-audacity -g -y
```

The `SKILL.md` files here are the canonical repo-root copies. Installed harness
packages still ship compatibility copies inside `tarunai_connect/<software>/skills/`
for local runtime discovery.

CI rule:

- If a harness keeps a deep packaged `SKILL.md`, it must also have a matching
  repo-root `skills/<skill-id>/SKILL.md`.
- A future harness that only defines its canonical skill directly in `skills/`
  is also valid.
