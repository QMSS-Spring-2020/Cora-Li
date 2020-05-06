# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:09:46 2020

@author: licor
"""

def summarizer(text, percentage):
    import en_core_web_sm
    from nltk.corpus import stopwords
    from string import punctuation
    stop_words = set(stopwords.words('english'))
    nlp = en_core_web_sm.load()
    
    doc = nlp(text)
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
                    
    max_frequency = max(word_frequencies.values())              
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency
    
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    from heapq import nlargest
    select_length = int(len(sentence_tokens)*percentage)
    if select_length < 1:
        summary = nlargest(1, sentence_scores, key = sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
    else:
        summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
    
    return summary