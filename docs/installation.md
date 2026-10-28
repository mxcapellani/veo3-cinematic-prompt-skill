# Installation and updates

Clone `https://github.com/mxcapellani/veo3-cinematic-prompt-skill.git` or download the repository. Copy `.agents/skills/veo3-cinematic-director/` to the host-supported skills directory. Keep the folder name and references intact. Explicit activation may use `veo3-cinematic-director` if the host supports named skills.

Smoke test with a short scene description and then a PT-BR quotation. Confirm technical English, unchanged quotation, camera/light/sound and one copyable prompt block. This is a manual behaviour check, not automatically performed by installation.

For updates, retain customizations separately, read changelog, replace the whole skill folder with a validated version and rerun structural and relevant behavioural tests. Provider credentials, when needed for rendering, belong in the provider's secure configuration, never in this repository or chat.
