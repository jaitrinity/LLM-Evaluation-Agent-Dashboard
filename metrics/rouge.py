from rouge_score import rouge_scorer

def rouge(reference, prediction):

    if isinstance(reference, list):
        reference = " ".join(reference)

    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

    scores = scorer.score(reference, prediction)

    return scores['rougeL'].fmeasure