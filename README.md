# Veo 3 Cinematic Director — Ultimate Agent Skill

Version 1.0.0.

Professional Agent Skill for Google Veo 3 cinematic prompt engineering, Brazilian Portuguese dialogue, camera direction, lighting, audio design, visual continuity, and production-ready video prompts.

## Purpose
Turn short ideas and detailed briefs into usable audiovisual direction. The default workflow is direct description-to-prompt, without a mandatory interview. This is a textual director, not a renderer, Google API client or official Google product.

## Preserved capabilities and evidence
The authorized migration brief documents scene expansion, subject/setting/action, cinematography, light, sound, exact spoken dialogue and copyable output. No original-agent response samples were supplied, so these are documented requirements rather than runtime-verified parity. See [migration audit](docs/migration-audit.md).

## Ultimate procedures
Ten modes cover automatic and advanced prompts, Brazilian dialogue, short idea expansion, revision, diagnosis, variations, sequences, references and platform adaptation. Added operational checks address physics, complexity, timing, exact dialogue, sound hierarchy and continuity. They do not guarantee generator compliance.

## Quick example
Input: “Uma mulher entra em um ônibus no Rio de Janeiro e diz: 'Moço, esse ônibus passa na Central?'”

Expected form: technical English in one copyable block with a dedicated SPOKEN TEXT (Portuguese - BR) section containing the exact Portuguese line and speaker. See the [complete example](.agents/skills/veo3-cinematic-director/examples/brazilian-dialogue.md).

## Installation and use
Copy `.agents/skills/veo3-cinematic-director/` into the discovery directory accepted by the host. See [installation](docs/installation.md) and [usage](docs/usage.md). Publishing the repository does not automatically install the Skill in ChatGPT.

The [self-contained SKILL.md](.agents/skills/veo3-cinematic-director/SKILL.md) contains essential rules; eight references deepen techniques and six examples demonstrate complete outputs. Docs explain architecture, compatibility and evidence. Tests contain machine-readable cases, acceptance criteria, comparison and a rubric.

## Compatibility and dependencies
Basic prompt writing needs no external service, API key or browsing. Optional vision, video access and documentation lookup depend on the host. Veo 3 is the intended creative destination; current platform/version limits and API compatibility are not claimed as tested. Do not infer a rigid duration when the user has not specified one.

## Validation
```bash
python -m pip install -r tests/requirements.txt
python tests/validate.py
python tests/test_validator.py
```
Python 3.9+ and PyYAML 6.x. Dependency installation may need network access; validation itself uses local files and no credentials. CI runs structural checks on push and pull request. These checks do not measure visual quality, speech naturalness or model performance.

## Limitations and test status
The [acceptance suite](tests/acceptance-tests.md) and [comparison matrix](tests/comparison-matrix.md) are planned, not executed against the original agent or a video model. Verbatim dialogue can be checked textually; pronunciation and lip-sync need real rendered media. No guaranteed identity preservation, scene reproducibility or provider feature support.

## Updates and contributions
Use semantic versioning, retain dialogue and output contracts, update examples and record regressions. See [CONTRIBUTING](CONTRIBUTING.md) and [CHANGELOG](CHANGELOG.md). The full source brief is preserved in [source specification](docs/source-specification.md).

## License
MIT, copyright 2026 mxcapellani, following the repository owner's established licensing choice. This independently authored implementation does not imply Google endorsement or ownership of third-party assets.

## Em português
Esta Skill transforma ideias em prompts de vídeo: direção técnica em inglês, falas PT-BR preservadas literalmente, câmera/luz/áudio coerentes e saída pronta para copiar. A validação estrutural não comprova equivalência ao agente original nem renderização no Veo.
