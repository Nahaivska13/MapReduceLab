import re
from src.core.job.mapper import Mapper

WORD_RE = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*")
VOWELS = set("aeiouyаеєиіїоуюя")   # англійські + українські

class VowelConsonantMapper(Mapper):
    def map(self, record, emit):
        for word in WORD_RE.findall(str(record).lower()):
            letters = [ch for ch in word if ch.isalpha()]
            if not letters:
                continue
            v = sum(ch in VOWELS for ch in letters)
            c = len(letters) - v
            emit(len(letters), [v, c, 1])
