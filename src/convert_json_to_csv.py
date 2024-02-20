import datetime
import os
import pandas as pd
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="./config", config_name="dev")
def main(cfg: DictConfig):
  # Main entry point for the pipeline.
  OmegaConf.to_yaml(cfg)

  # REF: https://www.geeksforgeeks.org/convert-nested-json-to-csv-in-python/


if __name__ == '__main__':
  x = main()