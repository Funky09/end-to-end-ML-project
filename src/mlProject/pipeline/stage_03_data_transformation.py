from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path
import pdb




class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        with open(Path("artifacts/data_validation/status.txt"),'r') as f:
            status = f.read().split(" ")[-1]
        if status == 'True':
            try:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_spliting()

            except Exception as e:
                raise e
        else:
            raise Exception("your schema is not valid")

if __name__ == "__main__":
    STAGE_NAME = "Data Transformation Stage"
    try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n\n x===================x")
    
    except Exception as e:
        logger.exception(e)
        raise e
