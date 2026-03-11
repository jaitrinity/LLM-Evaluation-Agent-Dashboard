from nltk.translate.bleu_score import sentence_bleu

def bleu(reference, prediction):

    if isinstance(reference, list):
        reference = " ".join(reference)

    return sentence_bleu([reference.split()], prediction.split())