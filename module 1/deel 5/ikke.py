import re

def get_sub_sentences(text: str) -> list:
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|") 
    return [sentence.strip().lower() for sentence in sub_sentences if sentence.strip()]

def bereken_ego_score(sub_sentences: list) -> int:
    ego_score = 0
    for sentence in sub_sentences:
        words = sentence.split(' ')
        if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
            ego_score += 1
    return ego_score

text = 'ik ga morgen naar schoo. Mijn les begint vroeg'
sub_sentences = get_sub_sentences(text)
ego_score = bereken_ego_score(sub_sentences)
print("Ego Score:", ego_score)
