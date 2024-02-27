import datetime
import os
import pandas as pd
import hydra
import json
from omegaconf import DictConfig, OmegaConf
from glob import glob as glob

# TODO: Investogate ** unpacking json

@hydra.main(config_path="./config", config_name="dev")
def main(cfg: DictConfig):
  # Main entry point for the pipeline.
  OmegaConf.to_yaml(cfg)

  # REF: https://www.geeksforgeeks.org/convert-nested-json-to-csv-in-python/

  # Get current working directory
  cwd = os.getcwd()

  # Set read path as staging path
  read_path = write_path = f"{cwd}{cfg.storage.staging.file_path}"
  print(f"---->>>> Read path: {read_path}")

  def read_json(filename: str) -> dict: 
    try: 
        with open(filename, "r") as f: 
            data = json.loads(f.read()) 
    except: 
        raise Exception(f"Reading {filename} file encountered an error")
    
    return data 

  # Write to csv
  # data.to_csv(f'{read_path}/competitions_2024-02-15.csv', index=False)
                                                                                       
  # results = glob(read_path + "*.json", recursive=False)
  # [print(z) for z in results]
  # paths = Path("/home/data").glob("*.json")
  # df = pd.DataFrame([pd.read_json(p, typ="series") for p in paths])


if __name__ == '__main__':
  x = main()