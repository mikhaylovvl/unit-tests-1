import unittest
from main import delete_doc, check_document_existance, add_new_doc, get_doc_owner_name
from parameterized import parameterized

fixture = [
    ("2207 876234", True),
    ("11-2", True),
    ("10006", True),
    ("106", False)
]
fixture_doc_owner_name = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("106", "")
]

fixture_add_new_doc = [
    ("123", "passport", "Владимир Михайлов", 4, 4),
    ("456", "passport", "Василий Захарченко", 5, 5)
]


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp ===> Start test")

    def tearDown(self) -> None:
        print("tearDown ===> End test")

    @parameterized.expand(fixture)
    def test_a_check_document_existance(self, doc_number, result):
        calc_result = check_document_existance(doc_number)
        self.assertEqual(calc_result, result)

    @parameterized.expand(fixture_doc_owner_name)
    def test_b_get_doc_owner_name(self, doc_number, result):
        calc_result = get_doc_owner_name(doc_number)
        self.assertEqual(calc_result, result)

    @parameterized.expand(fixture_add_new_doc)
    def test_c_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result):
        result = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
        self.assertEqual(result, expected_result)

    @parameterized.expand(fixture)
    def test_d_delete_doc(self, doc_number, result):
        calc_result = delete_doc(doc_number)
        self.assertEqual(calc_result[1], result)
