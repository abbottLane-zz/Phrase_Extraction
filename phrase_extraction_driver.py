from pprint import pprint
from Extraction.PhraseExtractor import PhraseExtractor


def main():
   # init PhraseExtractor
    extractor = PhraseExtractor()

    # Load text from some file
    with open("Data/Spotify.txt", "rb") as f:
        full_text = f.read()

    # Try both methods for phrase extraction:
        # The NP Chunker method
    top_n_phrases_np_chunker = extractor.extract_top_n_phrases_METHOD1(full_text.decode('utf-8'), n=10)
        # The dependency parse arc method
    top_n_phrases_dep_parse = extractor.extract_top_n_phrases_METHOD2(full_text.decode('utf-8'), n=10)

    # Print results
    print("METHOD: NP Chunker:")
    pprint(top_n_phrases_np_chunker)
    print("METHOD: Dependency Parse Subtrees:")
    pprint(top_n_phrases_dep_parse)


if __name__=="__main__":
    main()
