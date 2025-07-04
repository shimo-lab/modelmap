def model_name2file_name(model_name: str) -> str:
    return model_name.replace('/', '_')


SEP = "\n" + "%" * 50 + "\n"

DATA_PATH = "../data/model-metadata/model-data-1018.pkl"
