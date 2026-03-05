import logging
import os
import glob
from rich.logging import RichHandler



def setup_logging(create_new_run=False) -> tuple[logging.Logger, str]:
    base_logs_dir = "Logs"
    os.makedirs(base_logs_dir, exist_ok=True)
    
    existing_logs = glob.glob(os.path.join(base_logs_dir, "log*"))
    max_num = 0
    for log_path in existing_logs:
        try:
            num = int(os.path.basename(log_path).replace("log", ""))
            max_num = max(max_num, num)
        except ValueError:
            continue
            
    if create_new_run:
        max_num += 1
        log_dir = os.path.join(base_logs_dir, f"log{max_num}")
        os.makedirs(log_dir, exist_ok=True)
    else:
        if max_num == 0:
            raise FileNotFoundError("No log directories found. Run Phase 1 first.")
        log_dir = os.path.join(base_logs_dir, f"log{max_num}")

    log_file_path = os.path.join(log_dir, "run.log")

    logger = logging.getLogger("IntegrationAgent")
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        logger.handlers.clear()

    rich_handler = RichHandler(rich_tracebacks=True, show_time=True)
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(rich_handler)
    logger.addHandler(file_handler)

    return logger, log_dir
