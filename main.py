from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipepline

Stage_name = "data Ingestion stage"

try:
    logger.info(f">>>>>>>> stage {Stage_name} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipepline()
    obj.main()
    logger.info(f">>>>>>>> stage {Stage_name} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
