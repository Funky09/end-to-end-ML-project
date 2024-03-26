
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        dataingestion_config = config.get_data_ingestion()
        dataingestion = DataIngestion(dataingestion_config)
        dataingestion.download_file()
        dataingestion.extract_zip_file()




if __name__ == "__main__":
    
    try:
        
        logger.info(f">>>>>>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<< STARTED")
        DT = DataingestionTrainingPipeline()
        DT.main()
        logger.info(f">>>>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<<<< COMPLETED \n\nx==========x")
    
    except Exception as e:
        raise e
