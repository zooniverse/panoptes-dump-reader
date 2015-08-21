import sys
import panoptes

def expand():
    df = panoptes.classifications.load_csv(sys.argv[1])
    print df.to_csv()
