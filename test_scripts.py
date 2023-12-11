import unittest
from unittest.mock import patch
import parser_helper
import nmap_analysis

class TestParserHelper(unittest.TestCase):
    def test_parse_nmap_xml(self):
        # Test the parse_nmap_xml function with a sample XML file
        result = parser_helper.parse_nmap_xml('path/to/sample_nmap_output.xml')
        self.assertEqual(result, "Expected result from parsing the XML file")

class TestNmapAnalysis(unittest.TestCase):
    @patch('nmap_analysis.openai.Completion.create')
    def test_query_openai(self, mock_create):
        # Mock the openai.Completion.create method
        mock_create.return_value = "this is a test resposne"

        # Call the query_openai function with a sample prompt
        response = nmap_analysis.query_openai("sample prompt")

        self.assert_Equal(response, "this is a test response")
        # Assert statements to check if the response is as expected

class TestRunAnalysis(unittest.TestCase):
    @patch('nmap_analysis.parse_nmap_xml')
    @patch('nmap_analysis.query_openai')
    def test_run_analysis(self, mock_parse, mock_query):
        # Mock the parse_nmap_xml and query_openai functions
        mock_parse.return_value = "Expected result from parsing the XML file"
        mock_query.return_value = "Expected response from OpenAI"

        # Call the run_analysis function with sample data
        nmap_analysis.run_analysis("sample api key", "path/to/sample_nmap_output.xml")

        self.assert_Equal(mock_parse.call_count, 1)


# Need to add more tests including error handling

if __name__ == '__main__':
    unittest.main()
