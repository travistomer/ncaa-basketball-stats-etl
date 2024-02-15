import datetime
import requests
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="./config", config_name="dev")
def main(cfg: DictConfig):
  # Main entry point for the pipeline.
  OmegaConf.to_yaml(cfg)

  response = requests.get(
    url=f"{cfg.api.base_url}{cfg.api.ncaa_basketball_endpoint}",
    headers=cfg.api.headers,
    verify=False,
  )

  print(response.json())


  


if __name__ == '__main__':
  x = main()