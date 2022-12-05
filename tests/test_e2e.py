from unittest import TestCase
from xml.dom.minidom import parseString
from secretary import Renderer

sample_data = {
    'loop': [
        1, True, 0, False, 'A string', u'Unicode V\xe1l\xfc\u1ebds', None,
        'True && True'
    ],
    'site': 'www.github.com'
}

class E2ETest(TestCase):
    def test_render(self):
        engine = Renderer()
        with open('./tests/e2e.fodt', 'rb') as template:
            output = engine.render(template, **sample_data)

        self.assertIn('Unicode Válüẽs', output.decode('utf-8'))
        self.assertIn('True &amp;&amp; True', output.decode('utf-8'))
        self.assertIn('www.github.com', output.decode('utf-8'))
        self.assertIn('True output', output.decode('utf-8'))
        self.assertNotIn('False output', output.decode('utf-8'))

        # Should not raises when parsing final xml
        parseString(output)
