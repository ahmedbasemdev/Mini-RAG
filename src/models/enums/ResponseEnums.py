from enum import Enum

class ResponseSignal(Enum):
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_VALIDATION_SUCCESS = "File validation successful"
    PROCESSING_FAILED = "Processing failed"
    PROCESSING_SUCCESS = "Processing successful"