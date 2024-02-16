import datetime
import json
import requests
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="./config", config_name="dev")
def main(cfg: DictConfig):
  # Main entry point for the pipeline.
  OmegaConf.to_yaml(cfg)

  # TODO: Add calss for api calls and error handling
  response = requests.get(
    url=f"{cfg.api.base_url}{cfg.api.ncaa_basketball_endpoint}",
    headers=cfg.api.headers,
    verify=False,
  )

  # Use the json module to load CKAN's response into a dictionary.
  response_dict = json.loads(response.text)

  # Construct file path
  write_path = f"{cfg.storage.staging.file_path}{cfg.storage.staging.file_name}_{str(response_dict['day']['date'])}.{cfg.storage.staging.file_type}"
  print(f"---->>>> {write_path}") # TODO: Convert to logger

  # TODO: Add error handling for file write and add class for file handling
  with open(write_path, 'w') as f: # Write file to staging
    json.dump(response_dict, f)


if __name__ == '__main__':
  x = main()