import sys

def error_message_detail(error, error_detail: sys):
    # sys.exc_info() returns (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()

    # Extract file name and line number where error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return message


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Generate the detailed message using the helper function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message