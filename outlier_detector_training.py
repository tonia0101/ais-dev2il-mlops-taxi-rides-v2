import sys
import logging
import mlflow
import json
import pickle
import os
from model_trainings import (
  train_random_forest_classifier,
  train_random_forest_classifier_v2,
  train_logistic_regression_classifier,
)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATA_FILE = "data/taxi-rides-training-data.parquet"

def train_model(model_type: str):
  logger.info("Training outlier detection classifier")

  valid_model_types = ['random_forest', 'random_forest_v2', 'logistic_regression']
  if model_type not in valid_model_types:
    raise ValueError(f"Unknown model_type '{model_type}'. Valid options: {', '.join(valid_model_types)}")

  if model_type == 'random_forest':
    model, metadata = train_random_forest_classifier(DATA_FILE)
  elif model_type == 'random_forest_v2':
    model, metadata = train_random_forest_classifier_v2(DATA_FILE)
  elif model_type == 'logistic_regression':
    model, metadata = train_logistic_regression_classifier(DATA_FILE)
  logger.info("Model training completed")

  os.makedirs("models", exist_ok=True)

  model_output_file = f"models/{model_type}.pkl"
  logger.info(f"Storing model to: {model_output_file}")
  with open(model_output_file, "wb") as f:
      pickle.dump(model, f)

  metadata_output_file = f"models/{model_type}.metadata.json"
  logger.info(f"Writing metadata to: {metadata_output_file}")
  with open(metadata_output_file, "w") as metadata_file:
      json.dump(metadata, metadata_file, indent=4)

  logger.info(metadata)

if __name__ == "__main__":
  model_type = sys.argv[1]  # random_forest, random_forest_v2, logistic_regression
  train_model(model_type)


