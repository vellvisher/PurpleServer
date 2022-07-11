import unittest
import newsletter_tool

class NewsletterToolTest(unittest.TestCase):

    def test_create_newsletter(self):
        html_file = 'tests/brew_golden.html'
        f = open(html_file)
        content = f.read()
        f.close()
        newsletter = newsletter_tool.create_newsletter(html_file)
        self.assertEqual(newsletter.provider, newsletter_tool.Provider.BREW)
        self.assertEqual(newsletter.newsletter_url, "https://raw.githubusercontent.com/vellvisher/PurpleServer/main/tests/brew_golden.html")
        self.assertGreater(newsletter.upload_time, 0)

    def test_create_articles(self):
        html_file = 'tests/brew_golden.html'
        f = open(html_file)
        content = f.read()
        f.close()

        newsletter = newsletter_tool.create_newsletter(html_file)
        self.assertEqual(newsletter.provider, newsletter_tool.Provider.BREW)
        self.assertEqual(newsletter.newsletter_url, "https://raw.githubusercontent.com/vellvisher/PurpleServer/main/tests/brew_golden.html")
        self.assertGreater(newsletter.upload_time, 0)

if __name__ == '__main__':
    unittest.main()
