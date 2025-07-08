import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize



def segmentar_em_frases_identificando_idioma(paragrafos_json):
    """
    Segmenta os textos de parágrafos em frases, identificando automaticamente o idioma com base no nome da coluna.

    Returns:
        lista de dicionários, cada um representando uma frase segmentada, com metadados.
    """
    frases_json = []

    for par in paragrafos_json:
        # Campos fixos
        base = {k: par[k] for k in par if k in ['source_book', 'paragraph_id', 'master_name', 'master_url']}
        
        for col, texto in par.items():
            if col in base or not isinstance(texto, str):
                continue

            col_lower = col.lower()
            if "illustration" in col_lower:
                continue  # ignora imagens

            # Identificação do idioma
            if "translation" in col_lower:
                lang = "en"
                lang_parameter = "english"

            elif "transcription" in col_lower or "transcribed" in col_lower:
                lang = "it"
                lang_parameter = "italian"

            else:
                lang = "unknown"
                lang_parameter = "english"


            frases = sent_tokenize(texto,lang_parameter) # usando o sent tokenize
            for i, frase in enumerate(frases):
                entrada = base.copy()
                entrada.update({
                    "sentence_id": i,
                    "lang": lang,
                    "field_name": col,
                    "text": frase
                })
                frases_json.append(entrada)

    return frases_json


def identificar_se_traducao_e_transcricao_sao_do_mesmo_manuscrito(traducao,transcricao):
    '''
        Verifica de onde eh a traducao, geralmente escrito após o (from the XXXX)
        Verifica se XXXX esta na coluna da transcricao
        se tiver, sao equivalentes então retorna XXXX
    '''
    return manuscript_name