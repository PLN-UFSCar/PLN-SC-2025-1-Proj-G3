# HEMAscraper
Repository for collecting HEMA public transcripted manuscripts and manuals, for science use

## Organização
Na pasta /Data teremos uma pasta para cada autor.
Dentro da pasta de cada autor, teremos suas obras separadas em pastas por capítulos, como estão no Wikitenauer. Ou seja se um autor tem apenas um livro, este estará dividido em capítulos.

Cada CSV representa um capítulo ou livro de um autor especifico.
Dentro do CSV cada coluna representa uma versão do livro, como são manuscritos, versões diferentes tem conteúdos diferentes. Assim como, estarão as traduções e transcrições dos livros.

| Título    | Versão | Autor | Tradutor/Transcritor | 
| ------------------------------------- | ------- | -------- | -------------------------- |
| DE LO SCHERMO OVERO SCIENZA D’ARME    | Archetype (1606) | Salvator Fabris | Transcribed by Michael Chidester |
| DE LO SCHERMO OVERO SCIENZA D’ARME Draft Translation  | (ca. 1900) from the Archetype (1606) | Salvator Fabris | A. F. Johnson (transcribed by Michael Chidester) |
| Fior di Battaglia    | Novati (1400s) | Fiore Furlano de’i Liberi | Transcribed by Michael Chidester | 
| Fior di Battaglia    | Novati (1400s) | Fiore Furlano de’i Liberi | Translation by Colin Hatcher Transcribed by Michael Chidester | 
| Fior di Battaglia    | Morgan (1400s) | Fiore Furlano de’i Liberi | Transcribed by Michael Chidester | 
| Fior di Battaglia    | Getty (1400s) | Fiore Furlano de’i Liberi | Transcribed by Michael Chidester | 

# Pasata Scripts

Este diretório **scripts** reúne todos os arquivos necessários para extração, pré-processamento, pós-processamento, tradução e avaliação de métricas de qualidade de corpus textuais. A seguir, uma descrição de cada componente:

---

## Estrutura de Arquivos

- **Alimentar\_openai.py**

  - Implementa o pipeline de processamento de textos e pós-processamento (PP). Integra chamadas à API OpenAI.

- **Alimentar\_openai\_eng\_pt.py**

  - Versão advinda do italiano (italiano → inglês → português) do pipeline.

- **Alimentar\_openai\_eng\_pt\_direct.py**

  - Pipeline direto do inglês para português sem etapas intermediárias de fallback.

- **Alimentar\_openai\_it\_eng.py**

  - Pipeline de tradução de italiano para inglês.

- **GetTheCorpus.ipynb**

  - Notebook para coleta e exploração inicial do corpus.

- **Metricas.py**

  - Cálculo automatizado de métricas de avaliação (BLEU, chrF, etc.) para comparações de tradução.

- **Pipeline.md**

  - Documentação detalhada do fluxo de trabalho (diagrama, etapas e dependências).

- **PosProcessamento.py**

  - Módulo de pós-processamento de saídas, limpeza e normalização final.

- **PreProcessamento.py**

  - Módulo de pré-processamento de textos (tokenização, normalização, limpeza).

- **Textos.rar**

  - Arquivo compactado contendo os textos já pós-processados e resultados de interseção.

- **Traducao.py**

  - Funções genéricas de tradução, abstraindo diferentes serviços e estratégias.

- **WikitenauerScrapper.py**

  - Script de scraping para extrair textos do repositório Wikitenauer.

---

## Dados e Checkpoints

- **corpus.jsonl**

  - Arquivo principal do corpus bruto em formato JSON Lines.

- **corpus\_sentences.jsonl**

  - Corpus segmentado em sentenças.

- **corpus\_sentences\_openai\_eng.jsonl**

  - Sentenças traduzidas (OpenAI) italiano → inglês.

- **corpus\_sentences\_openai\_eng\_pt.jsonl**

  - Sentenças traduzidas em inglês e pós-processadas para português.

- **corpus\_sentences\_openai\_eng\_pt\_direct.jsonl**

  - Tradução direta inglês→português.

- **corpus\_sentences\_openai\_pt.jsonl**

  - Sentenças traduzidas diretamente para português.

- **checkpoint\_openai.json**, **checkpoint\_openai\_eng.json**, **checkpoint\_openai\_eng\_pt.json**

  - Arquivos de ponto de verificação para retomada de processos da API OpenAI.

---

## Visualizações e Avaliações

- **bleu\_comparison.png**

  - Gráfico comparativo de BLEU entre diferentes estratégias.

- **grafico\_avaliacao.png**, **grafico\_avaliacao\_2.png**, **grafico\_avaliacao\_3.png**

  - Imagens de métricas manuais e automáticas comparadas.

- **metricas\_heatmap.png**

  - Heatmap de similaridades entre interseções de corpora.

- **nuvem\_palavras.py**

  - Gera nuvem de palavras para visualização de frequência.

- **grafico\_avaliacao.py**, **grafico\_avaliacao\_2.py**, **grafico\_avaliacao\_3.py**

  - Scripts para gerar os gráficos de avaliação manual.

- **metricas\_heatmap.png**

  - Imagem do heatmap gerado.

---

## Auxiliares

- **intersecoes\_similares\_3\_pastas.txt**

  - Listagem textual de interseções similares entre três pastas de resultados.

- **organizar\_intersecoes\_similares.py**

  - Script para organizar e agrupar interseções similares.

---

## Como Usar

1. Clone o repositório e navegue até `scripts/`.
2. Prepare seu ambiente virtual Python e instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute `GetTheCorpus.ipynb` para coletar e inspeccionar o corpus.
4. Use `PreProcessamento.py` para pipeline de limpeza.
5. Rode os pipelines de tradução via OpenAI (`Alimentar_openai*.py`).
6. Use 'PosProcessamento.py'
7. Avalie resultados com `Metricas.py` e visualize com os scripts em `*.py`.

---
