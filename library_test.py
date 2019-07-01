import unittest
import library

NUM_CORPUS = '''
On the 5th of May every year, Mexicans celebrate Cinco de Mayo. This tradition
began in 1845 (the twenty-second anniversary of the Mexican Revolution), and
is the 1st example of a national independence holiday becoming popular in the
Western Hemisphere. (The Fourth of July didn't see regular celebration in the
US until 15-20 years later.) It is celebrated by 77.9% of the population--
trending toward 80.
'''

class TestCase(unittest.TestCase):

    # Helper function
    def assert_extract(self, text, extractors, *expected):
        actual = [x[1].group(0) for x in library.scan(text, extractors)]
        self.assertEqual(str(actual), str([x for x in expected]))

    # First unit test; prove that if we scan NUM_CORPUS looking for mixed_ordinals,
    # we find "5th" and "1st".
    def test_mixed_ordinals(self):
        self.assert_extract(NUM_CORPUS, library.mixed_ordinals, '5th', '1st')

    # Second unit test; prove that if we look for integers, we find four of them.
    def test_integers(self):
        self.assert_extract(NUM_CORPUS, library.integers, '1845', '15', '20', '80')
 
    def test_integers_2(self):
        self.assert_extract("I have 123,456,789 dollars", library.integers, '123,456,789')

    # Third unit test; prove that if we look for integers where there are none, we get no results.
    def test_no_integers(self):
        self.assert_extract("no integers", library.integers)

    # Prove that dates successfully extracted
    def test_dates_iso8601(self):
        self.assert_extract('I was born on 2015-07-25.', library.dates_iso8601, '2015-07-25')

    def test_bad_dates(self):
        self.assert_extract('I was born on 2015-13-25.', library.dates_iso8601)

    def test_bad_dates_2(self):
        self.assert_extract('I was born on 2015-07-32.', library.dates_iso8601)

    def test_new_date_format(self):
        self.assert_extract('I was born on 25 Jan 2017.', library.dates_other, '25 Jan 2017')
        # FIXME: Bad regex. Only works with period at the end

    def test_new_date_format_2(self):
        self.assert_extract('I was born on 25 Jan, 2017.', library.dates_other, '25 Jan, 2017')
        # FIXME: Bad regex. Only works with period at the end

    def test_third_date_format_1(self):
        self.assert_extract('I was born on 2018-06-22 18:22:19.123.', library.dates_third, '2018-06-22 18:22:19.123')

    def test_third_date_format_2(self):
        self.assert_extract('I was born on 2018-06-22 18:22:19', library.dates_third, '2018-06-22 18:22:19')

    def test_third_date_format_3(self):
        self.assert_extract('I was born on 2018-06-22 18:22', library.dates_third, '2018-06-22 18:22')

    def test_third_date_format_4(self):
        self.assert_extract('I was born on 2018-06-22 18', library.dates_third, '2018-06-22 18')

    def test_third_date_format_5(self):
        self.assert_extract('I was born on 2018-06-22 18:22:19.123Z.', library.dates_third, '2018-06-22 18:22:19.123Z')

    def test_third_date_format_6(self):
        self.assert_extract('I was born on 2018-06-22 18:22:19Z.', library.dates_third, '2018-06-22 18:22:19Z')

    def test_third_date_format_7(self):
        self.assert_extract('I was born on 2018-06-22 18:22Z.', library.dates_third, '2018-06-22 18:22Z')
    def test_third_date_format_8(self):
        self.assert_extract('I was born on 2018-06-22 18Z.', library.dates_third, '2018-06-22 18Z')

    def test_third_date_format_9(self):
        self.assert_extract('I was born on 2018-06-22T18:22:19.123.', library.dates_third, '2018-06-22T18:22:19.123')

    def test_third_date_format_10(self):
        self.assert_extract('I was born on 2018-06-22T18:22:19', library.dates_third, '2018-06-22T18:22:19')
    def test_third_date_format_11(self):
        self.assert_extract('I was born on 2018-06-22T18:22', library.dates_third, '2018-06-22T18:22')
    def test_third_date_format_12(self):
        self.assert_extract('I was born on 2018-06-22T18', library.dates_third, '2018-06-22T18')

    def test_third_date_format_13(self):
        self.assert_extract('I was born on 2018-06-22T18:22:19.123Z.', library.dates_third, '2018-06-22T18:22:19.123Z')

    def test_third_date_format_14(self):
        self.assert_extract('I was born on 2018-06-22T18:22:19Z.', library.dates_third, '2018-06-22T18:22:19Z')

    def test_third_date_format_15(self):
        self.assert_extract('I was born on 2018-06-22T18:22Z.', library.dates_third, '2018-06-22T18:22Z')

    def test_third_date_format_16(self):
        self.assert_extract('I was born on 2018-06-22T18Z.', library.dates_third, '2018-06-22T18Z')

    def test_third_date_format_17(self):
        self.assert_extract('I was born on 2018-06-22T18:22:19.123MDT.', library.dates_third, '2018-06-22T18:22:19.123MDT')

    def test_third_date_format_18(self):
        self.assert_extract('I was born on 2018-06-22T18:22:19MDT', library.dates_third, '2018-06-22T18:22:19MDT')

    def test_third_date_format_19(self):
        self.assert_extract('I was born on 2018-06-22T18:22MDT.', library.dates_third, '2018-06-22T18:22MDT')

    def test_third_date_format_20(self):
        self.assert_extract('I was born on 2018-06-22T18MDT.', library.dates_third, '2018-06-22T18MDT')

if __name__ == '__main__':
    unittest.main()
