from analyzer.text_analyzer import (
    count_characters,
    count_paragraphs,
    count_sentences,
    count_words,
    longest_paragraph,
    longest_sentence,
    longest_word,
)

text = """
Hola perros, este texto es para analizar el programa.

En este texto habra al menos 5 oraciones.

Un ejemplo de oracion es: La casa de angel necesita unos arreglos.
"""

print("Palabras: ", count_words(text))
print("Caracteres: ", count_characters(text))
print("Párrafos: ", count_paragraphs(text))
print("Oraciones: ", count_sentences(text))
print("Párrafo más largo: ", longest_paragraph(text))
print("Palabra más larga: ", longest_word(text))
print("Oración más larga: ", longest_sentence(text))

