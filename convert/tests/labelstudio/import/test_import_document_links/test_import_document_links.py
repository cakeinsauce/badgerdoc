import json
from pathlib import Path
from tempfile import TemporaryDirectory

from convert.converters.base_format.badgerdoc import Badgerdoc
from convert.converters.labelstudio.labelstudio_to_badgerdoc_converter import (
    ConverterToBadgerdoc,
)
from convert.converters.labelstudio.models.annotation import LabelStudioModel

TEST_FILES_DIR = Path(__file__).parent / "data_annotations_with_links"


def test_import_document_links() -> None:
    badgerdoc_format = Badgerdoc()
    converter = ConverterToBadgerdoc()

    ls_model = LabelStudioModel.parse_file(TEST_FILES_DIR / "labelstudio.json")
    converter.to_badgerdoc(ls_model)
    badgerdoc_format.tokens_page = converter.tokens_page
    badgerdoc_format.remove_non_printing_tokens()
    converter.tokens_page = badgerdoc_format.tokens_page
    converter.to_badgerdoc_annotations(ls_model)
    badgerdoc_format.badgerdoc_annotation = (
        converter.badgerdoc_annotation
    )
    with TemporaryDirectory() as dir_name:
        # test tokens
        tokens_test_path = Path(dir_name) / "tokens_test.json"
        badgerdoc_format.export_tokens(tokens_test_path)
        tokens_test = json.loads(tokens_test_path.read_text())

        tokens_etalon_path = (
            TEST_FILES_DIR / "badgerdoc/tokens/1.json"
        )
        tokens_etalon = json.loads(tokens_etalon_path.read_text())
        assert tokens_test == tokens_etalon

        # test annotations
        annotations_test_path = Path(dir_name) / "annotations_test.json"
        badgerdoc_format.export_annotations(annotations_test_path)
        annotations_test = json.loads(annotations_test_path.read_text())
        annotations_etalon = json.loads((TEST_FILES_DIR / "badgerdoc/annotation/fixed.json").read_text())
        assert annotations_test == annotations_etalon
