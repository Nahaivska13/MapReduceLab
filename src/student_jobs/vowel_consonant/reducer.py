from src.core.job.reducer import Reducer

class VowelConsonantReducer(Reducer):
    def reduce(self, key, values, emit):
        v = c = n = 0
        for item in values:
            v += item[0]
            c += item[1]
            n += item[2]
        total = v + c
        emit(key, {
            "words": n,
            "avg_vowels": round(v / n, 3),
            "avg_consonants": round(c / n, 3),
            "vowels_pct": round(100 * v / total, 1),
            "consonants_pct": round(100 * c / total, 1),
            "consonants_to_vowels": round(c / v, 3) if v else None,
        })
