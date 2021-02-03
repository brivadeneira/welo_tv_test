import unittest

from justify_line import justify_text


class TestJustifyText(unittest.TestCase):

    def test_justify(self):
        text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera.'
        line_width = 30
        expected_justified_lines = [
            ['La ', ' historia', ' de', ' la', ' ópera', ' tiene'],
            ['una  ', ' duración  ', ' relativamente  '],
            ['corta ', ' dentro ', ' del', ' contexto', ' de'],
            ['la ', ' historia ', ' de ', ' la', ' música', ' en'],
            ['general: ', ' apareció ', ' en ', ' 1597, '],
            ['fecha  ', ' en ', ' que ', ' se ', ' creó ', ' la '],
            ['ópera.']]
        justified_lines = justify_text(text, line_width)
        self.assertEqual(justified_lines, expected_justified_lines)


    def test_wrong_width_number(self):
        with self.assertRaises(Exception) as context:
            text, line_width = 'a longword', 5
            justify_text(text, line_width)

        self.assertIn('A word length exceeds the long 5 width.',
                      str(context.exception))


if __name__ == '__main__':
    unittest.main()
