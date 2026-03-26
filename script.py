import logging
from datetime import datetime
import os
import argparse

# 🔹 Configure logging
logging.basicConfig(
    filename="file_processor.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def process_files(file1, file2):
    try:
        logging.info(f"Starting processing for {file1} and {file2}")

        # 🔹 Input validation
        if not file1 or not file2:
            raise ValueError("File names cannot be empty")

        if not isinstance(file1, str) or not isinstance(file2, str):
            raise TypeError("File names must be strings")

        if not os.path.exists(file1) or not os.path.exists(file2):
            raise FileNotFoundError("One or both files do not exist")

        # 🔹 Open files
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            data1 = f1.read()
            data2 = f2.read()

        # 🔹 Check empty file
        if len(data2) == 0:
            raise ZeroDivisionError("Second file is empty")

        # 🔹 Example processing
        length_ratio = len(data1) / len(data2)

        logging.info("Files processed successfully")

        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "file1_length": len(data1),
            "file2_length": len(data2),
            "ratio": length_ratio
        }

    # 🔹 Error Handling
    except ValueError as e:
        logging.error(f"Validation error: {e}")
        return f"Error: {e}"

    except TypeError as e:
        logging.error(f"Type error: {e}")
        return f"Error: {e}"

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return f"Error: {e}"

    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
        return "Error: Permission denied"

    except ZeroDivisionError as e:
        logging.error(f"{e}")
        return "Error: File2 is empty"

    except UnicodeDecodeError as e:
        logging.error(f"Encoding issue: {e}")
        return "Error: File encoding issue"

    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        return "Error: Unexpected issue occurred"

    finally:
        logging.info("Execution completed")


# 🔹 Command-line execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process two files safely")
    parser.add_argument("file1", help="Path to first file")
    parser.add_argument("file2", help="Path to second file")

    args = parser.parse_args()

    result = process_files(args.file1, args.file2)
    print(result)
