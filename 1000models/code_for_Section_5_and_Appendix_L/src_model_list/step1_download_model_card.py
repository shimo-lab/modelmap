import logging
import pickle as pkl
from pathlib import Path

from huggingface_hub import ModelCard
from tqdm import tqdm
from utils import DATA_PATH, model_name2file_name

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main():

    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)

    model_names = [tmp["model_name"] for tmp in modeldata]

    md_dir = Path("data/model_cards")
    md_dir.mkdir(parents=True, exist_ok=True)

    for model_name in tqdm(model_names):
        file_name = model_name2file_name(model_name)
        md_path = md_dir / f"{file_name}.md"

        try:
            logger.info(f"Downloading model card for {model_name}...")
            card = ModelCard.load(model_name)

            md_text = card.text
            with open(md_path, "w") as f:
                f.write(md_text)

        except Exception as e:
            logger.error(f"{model_name} failed: {e}")


if __name__ == "__main__":
    import fire
    fire.Fire(main)
