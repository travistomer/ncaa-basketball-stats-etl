import datetime
import requests
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="./config", config_name="dev")
def main(cfg: DictConfig):
  # Main entry point for the pipeline.
  print(OmegaConf.to_yaml(cfg))
  


if __name__ == '__main__':
  x = main()