# Acceptance tests

All behavioural cases are NOT EXECUTED. Machine-readable inputs and assertions are in test-cases.json. Prior-context tests must receive the same frozen prerequisites; image tests require the same actual authorized assets.

## T01 — simple

Complexity: simple.

Input: Um homem está caminhando por uma praia ao pôr do sol.

Expected: subject, environment, action, camera, lighting and ambient sound; no unsolicited dialogue.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T02 — dialogue

Complexity: intermediate.

Input: Uma mulher entra em um ônibus no Rio de Janeiro e diz: 'Moço, esse ônibus passa na Central?'

Expected: exact supplied line; SPOKEN TEXT (Portuguese - BR); speaker and lip-sync direction; English technical content.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T03 — drama

Complexity: intermediate.

Input: Um homem recebe uma notícia inesperada durante uma noite chuvosa.

Expected: readable performance; motivated dramatic light; rain sound; no invented news content.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T04 — advertisement

Complexity: intermediate.

Input: Uma câmera revela lentamente um carro esportivo estacionado em um estúdio escuro.

Expected: controlled reveal; coherent reflections; car remains stationary; no invented brand claims.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T05 — camera-conflict

Complexity: regression.

Input: Corrija: câmera Static e Orbit simultaneamente, sem cortes.

Expected: resolve simultaneous conflict; continuous shot; preserve purpose.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T06 — sequence

Complexity: advanced.

Input: Crie três cenas de uma pessoa entrando num café, encontrando alguém e iniciando conversa.

Expected: three independent blocks; wardrobe/prop/geography anchors; ordered states; no fabricated spoken line.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T07 — verbatim

Complexity: regression.

Input: A pessoa fala exatamente: “Hoje eu vim aprender, não fingir que já sei.”

Expected: exact quotation; no translation; speaker attribution.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T08 — multiple-speakers

Complexity: advanced.

Input: Ana diz “Você chegou.” Bruno responde “Cheguei agora.”

Expected: two attributed exact lines; no speaker swap; turn order.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T09 — silence

Complexity: regression.

Input: Uma biblioteca em silêncio absoluto, sem voz, efeitos ou música.

Expected: no added ambience contrary to silence; clear visual action.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T10 — ambience-only

Complexity: intermediate.

Input: Chuva na janela, somente áudio ambiente, sem música e sem fala.

Expected: rain bed; no music; no speech.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T11 — duration-conflict

Complexity: error.

Input: Esta fala de 45 palavras precisa caber em dois segundos sem alteração.

Expected: expose time conflict; do not silently shorten; offer material alternatives.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T12 — continuous

Complexity: regression.

Input: Um único plano contínuo acompanhando uma pessoa entrando num quarto; sem cortes ou transições.

Expected: no montage; continuous camera path; ordered entry.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T13 — missing-reference

Complexity: error.

Input: Reproduza a imagem que não foi anexada.

Expected: request image; do not claim visual observation.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T14 — stylized

Complexity: intermediate.

Input: Uma raposa de animação em aquarela atravessa um jardim.

Expected: respect stylization; do not impose photorealism; coherent motion.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T15 — unknown-platform

Complexity: error.

Input: Adapte para um gerador desconhecido com parâmetros não documentados.

Expected: portable text; no invented proprietary syntax; state uncertainty.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T16 — variations

Complexity: advanced.

Input: Três versões: documental, dramática e publicitária, preservando esta ação e fala anterior.

Expected: same prerequisite context in both environments; three distinct treatments; fixed dialogue preserved.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T17 — quantity-format

Complexity: regression.

Input: Entregue somente um prompt final em inglês, com a fala “Tudo certo.” em português.

Expected: one block; no external commentary; exact dialogue.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T18 — reference

Complexity: advanced.

Input: Use a imagem A para personagem e B para ambiente, mantendo roupa de A.

Expected: actual accessible images required; roles separated; no identity mixing.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T19 — render-claim

Complexity: error.

Input: Você já renderizou o vídeo?

Expected: do not claim rendering without tool execution.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.

## T20 — prop-continuity

Complexity: advanced.

Input: Uma pessoa segura um caderno na mão esquerda, abre a porta e entra, sem trocar de roupa.

Expected: prop ownership stable; plausible hand/door action; wardrobe unchanged.

Original output: not available. Skill output: not executed. Score: not assigned. Result: NOT EXECUTED. Evidence: none. Notes: record host, model, date, references and full outputs at execution.
