from goodreads_api_client.resources import Book
from goodreads_api_client.tests.resources import ResourceTestCase, vcr


class TestBook(ResourceTestCase):
    def setUp(self):
        self._book = Book(transport=self._transport)

    @vcr.use_cassette('book/id_to_work_id.yaml')
    def test_id_to_work_id(self):
        result = self._book.id_to_work_id(['1842', '1867'])

        self.assertEqual(result['item'], ['2138852', '5985'])

    @vcr.use_cassette('book/review_counts.yaml')
    def test_review_counts(self):
        result = self._book.review_counts(['0441172717', '0141439602'])

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], {
            'id': 53732,
            'isbn': '0441172717',
            'isbn13': '9780441172719',
            'ratings_count': 8529,
            'reviews_count': 14303,
            'text_reviews_count': 747,
            'work_ratings_count': 525005,
            'work_reviews_count': 800918,
            'work_text_reviews_count': 13207,
            'average_rating': '4.19',
        })

    @vcr.use_cassette('book/show.yaml')
    def test_show(self):
        book_dict = self._book.show('50')

        self.assertEqual(book_dict['id'], '50')
        self.assertEqual(book_dict['title'], "Hatchet (Brian's Saga, #1)")

    @vcr.use_cassette('book/show_by_isbn.yaml')
    def test_show_by_isbn(self):
        result = self._book.show_by_isbn('0441172717')

        self.assertEqual(result['id'], '53732')
        self.assertEqual(result['title'], 'Dune')
