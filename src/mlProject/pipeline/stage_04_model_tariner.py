from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path
import pdb


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_data_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train_model()

        except Exception as e:
            raise e
       










if __name__ == "__main__":
    STAGE_NAME = "Model Trainer"
    try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n\n x===================x")
    
    except Exception as e:
        logger.exception(e)
        raise e