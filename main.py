from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipepline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline

Stage_name = "data Ingestion stage"

try:
    logger.info(f">>>>>>>> stage {Stage_name} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipepline()
    obj.main()
    logger.info(f">>>>>>>> stage {Stage_name} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "prepare base model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e