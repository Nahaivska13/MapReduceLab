import re
from src.core.job.mapper import Mapper

WORD_RE = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*")

class CleanWordCountMapper(Mapper):
    def map(self, record, emit):
        for word in WORD_RE.findall(str(record).lower()):
            emit(word, 1)





