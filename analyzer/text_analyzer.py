def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def count_sentences(text):
    sentences = text.split('.')
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def count_paragraphs(text):
    paragraphs = text.split('\n\n')
    paragraphs = [p for p in paragraphs if p.strip()]
    return len(paragraphs)

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def longest_setence(text):
    sentences = text.split('.')
    sentences = [s for s in sentences if s.strip()]
    if not sentences:
        return ""
    return max(sentences, key=len)

def longest_paragraph(text):
    paragraphs = text.split('\n\n')
    paragraphs = [p for p in paragraphs if p.strip()]
    if not paragraphs:
        return ""
    return max(paragraphs, key=len)
