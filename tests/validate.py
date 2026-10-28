#!/usr/bin/env python3
"""Validação estrutural local; não mede comportamento ou qualidade de imagens."""
from pathlib import Path
import re
import sys
import yaml

BASE = ".agents/skills/veo3-cinematic-director"
REQUIRED = ['.agents/skills/veo3-cinematic-director/SKILL.md', '.agents/skills/veo3-cinematic-director/references/cinematography.md', '.agents/skills/veo3-cinematic-director/references/camera-and-lenses.md', '.agents/skills/veo3-cinematic-director/references/lighting-and-color.md', '.agents/skills/veo3-cinematic-director/references/audio-and-dialogue.md', '.agents/skills/veo3-cinematic-director/references/brazilian-portuguese.md', '.agents/skills/veo3-cinematic-director/references/continuity.md', '.agents/skills/veo3-cinematic-director/references/prompt-patterns.md', '.agents/skills/veo3-cinematic-director/references/quality-checklist.md', '.agents/skills/veo3-cinematic-director/examples/simple-scene.md', '.agents/skills/veo3-cinematic-director/examples/brazilian-dialogue.md', '.agents/skills/veo3-cinematic-director/examples/cinematic-advertisement.md', '.agents/skills/veo3-cinematic-director/examples/dramatic-scene.md', '.agents/skills/veo3-cinematic-director/examples/prompt-revision.md', '.agents/skills/veo3-cinematic-director/examples/multi-scene-sequence.md', 'docs/source-specification.md', 'docs/installation.md', 'docs/usage.md', 'docs/architecture.md', 'docs/compatibility.md', 'docs/migration-audit.md', 'tests/acceptance-tests.md', 'tests/comparison-matrix.md', 'tests/evaluation-rubric.md', 'tests/test-cases.json', 'tests/validate.py', 'tests/test_validator.py', 'tests/requirements.txt', '.github/workflows/validate.yml', 'README.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md', '.gitignore']

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Chave YAML duplicada: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def validate(root):
    root = Path(root).resolve()
    errors = []
    for rel in REQUIRED:
        p = root / rel
        if not p.is_file() or not p.stat().st_size:
            errors.append(f"Arquivo ausente ou vazio: {rel}")
    skill = root / BASE / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            errors.append("Frontmatter YAML deve iniciar na primeira linha e ter fechamento.")
        else:
            try:
                data = yaml.load(match.group(1), Loader=UniqueLoader)
                if not isinstance(data, dict):
                    raise ValueError("Frontmatter precisa ser um mapa.")
                if data.get("name") != "veo3-cinematic-director":
                    errors.append("Nome técnico incorreto.")
                desc = data.get("description")
                if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
                    errors.append("Description deve ser texto não vazio com até 1024 caracteres.")
                allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
                if set(data) - allowed:
                    errors.append("Campos YAML desconhecidos.")
            except (yaml.YAMLError, ValueError, TypeError) as exc:
                errors.append(f"YAML inválido: {exc}")
        for heading in ("automatic modes", "brazilian portuguese dialogue", "response structure", "final quality check"):
            if heading not in text.lower():
                errors.append(f"Seção essencial ausente: {heading}")
    for p in root.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        # Marcadores proibidos são de entrega incompleta, não exemplos de prompts.
        if re.search(r"\b(?:TODO|FIXME)\b|SEU-USUARIO|\[NOME-DO-TITULAR\]|<placeholder>", text):
            errors.append(f"Marcador não resolvido: {p.relative_to(root)}")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or re.match(r"[a-zA-Z][\w+.-]*:", target):
                continue
            dest = (p.parent / target).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"Link interno inválido: {p.relative_to(root)} -> {target}")
    tests = root / "tests/acceptance-tests.md"
    if tests.is_file():
        ids = re.findall(r"^## (T\d{2}) —", tests.read_text(encoding="utf-8"), re.M)
        if len(ids) < 20 or len(ids) != len(set(ids)):
            errors.append("Exigir pelo menos 20 casos únicos de aceitação.")
    workflow = root / ".github/workflows/validate.yml"
    if workflow.is_file():
        try:
            wf = yaml.load(workflow.read_text(encoding="utf-8"), Loader=UniqueLoader)
            if not isinstance(wf, dict) or not {"push", "pull_request"} <= set(wf.get("on", {})):
                errors.append("Workflow precisa executar em push e pull_request.")
            if "python tests/validate.py" not in workflow.read_text(encoding="utf-8"):
                errors.append("Workflow não executa o validador.")
        except (yaml.YAMLError, ValueError, TypeError) as exc:
            errors.append(f"Workflow inválido: {exc}")
    cases_file = root / "tests/test-cases.json"
    if cases_file.is_file():
        import json
        try:
            cases = json.loads(cases_file.read_text(encoding="utf-8"))
            if not isinstance(cases, list) or len(cases) != 20:
                errors.append("Require twenty machine-readable cases.")
            elif [c.get("id") for c in cases] != [f"T{i:02d}" for i in range(1,21)]:
                errors.append("Case IDs are missing or duplicated.")
        except (ValueError, AttributeError, TypeError) as exc:
            errors.append(f"Invalid cases JSON: {exc}")
    dialogue_example = root / BASE / "examples/brazilian-dialogue.md"
    if dialogue_example.is_file():
        content = dialogue_example.read_text(encoding="utf-8")
        if "SPOKEN TEXT (Portuguese - BR)" not in content or '"Moço, esse ônibus passa na Central?"' not in content:
            errors.append("Dialogue example lost exact speech or heading.")
    sequence = root / BASE / "examples/multi-scene-sequence.md"
    if sequence.is_file() and len(re.findall(r"^## Scene \d+", sequence.read_text(encoding="utf-8"), re.M)) != 3:
        errors.append("Sequence example requires three independent scenes.")
    return errors

if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(f"ERRO: {error}")
    if not errors:
        print(f"OK: {len(REQUIRED)} arquivos; YAML, referências e 20 casos verificados. Comportamento não avaliado.")
    sys.exit(bool(errors))
