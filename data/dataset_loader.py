from sklearn.datasets import fetch_20newsgroups

def load_dataset():
    
    dataset = fetch_20newsgroups(
        subset="all",
        remove=("headers", "footers", "quotes")
    )

    texts = dataset.data
    labels = dataset.target

    print("Total documents:", len(texts))

    return texts, labels