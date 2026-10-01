import sys
import os

#Agregar ruta de paquetes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzer.text_analyzer import (count_words,
                                    count_characters, 
                                    count_sentences,
                                    longest_word)

def test_count_words():
    text = "This is a sample text."
    assert count_words(text) == 5

def test_count_characters():
    text = "This is a sample text."
    assert count_characters(text) == 23

def test_count_characters():
    text = "hola"
    assert count_characters(text) == 4

def test_count_sentences():
    text = "This is a sample text. It has two sentences."
    assert count_sentences(text) == 2

def test_longest_word():
    text = "This is a sample text."
    assert longest_word(text) == "sample"

if __name__ == "__main__":
    print("Running tests...")
    test_count_words()
    test_count_characters()
    test_count_sentences()
    test_longest_word()
    print("All tests passed.")