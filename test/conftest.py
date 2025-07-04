import pytest
from fastapi import UploadFile
from io import BytesIO

@pytest.fixture
def mock_upload_file():
    def _mock_upload_file(content: bytes, filename: str = "test.docx"):
        """

        :type content: bytes
        """
        return UploadFile(filename=filename, file=BytesIO(content))
    return _mock_upload_file