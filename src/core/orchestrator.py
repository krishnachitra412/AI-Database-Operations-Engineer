from src.utils.logger import log_info, log_error
from src.core.pipeline import run_pipeline

def execute():

    try:
        log_info("Pipeline execution started")

        result = run_pipeline()

        log_info("Pipeline execution completed")

        return result

    except Exception as e:
        log_error(str(e))
        raise