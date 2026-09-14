# ORPHEUS Security Boundary & Policy

## Absolute Rules
1. **Zero Secret Policy**: No API keys, tokens, passwords, cookies, auth files, or Telegram credentials may ever be committed or pushed to GitHub or Hugging Face.
2. **Local State Protection**: Runtime state, gateway PIDs, logs, and SQLite databases remain strictly local.
3. **No Full Mirroring**: Full profiles or local state folders of Hermes/9Router are excluded via `.gitignore`.
