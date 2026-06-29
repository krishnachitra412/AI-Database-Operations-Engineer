from src.core.pipeline import run_pipeline
from src.utils.logger import log_info, log_error

def execute():

    try:
        log_info("Pipeline execution started")

        result = run_pipeline()

        log_info(f"Pipeline completed with {len(result['incidents'])} incidents")

        return result

    except Exception as e:
        log_error(f"Pipeline failed: {str(e)}")
        raise