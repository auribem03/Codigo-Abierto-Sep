import os
import sys

# Agregar ruta de paquetes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzer.text_analyzer import (
    count_characters,
    count_sentences,
    count_words,
    longest_word,
)


def test_count_words():
    text = "This is a sample text"
    assert count_words(text) == 5


def test_count_characters():
    text = "This is a sample text."
    assert count_characters(text) == 22


def test_count_characters_short():
    text = "hola"
    assert count_characters(text) == 4


def test_count_sentences():
    text = "Hello world. This is a test."
    assert count_sentences(text) == 2
    #hola


def test_longest_word():
    text = "The quick brown fox jumps over the lazy dog"
    assert longest_word(text) == "quick"