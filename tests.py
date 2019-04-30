import unittest
from anagram import substringAnagrams

class TestAnagram(unittest.TestCase):

  def test_a(self):
    self.assertEqual(substringAnagrams("a"), 0)

  def test_aa(self):
    self.assertEqual(substringAnagrams("aa"), 1)

  def test_aaa(self):
    self.assertEqual(substringAnagrams("aaa"), 4)

  def test_aaaa(self):
    self.assertEqual(substringAnagrams("aaaa"), 10)

  def test_aaaaaaaaa(self):
    self.assertEqual(substringAnagrams("aaaaaaaaa"), 120)

  def test_40_a(self):
    self.assertEqual(substringAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), 10660)

  def test_abba(self):
    self.assertEqual(substringAnagrams("abba"), 4)

  def test_abcd(self):
    self.assertEqual(substringAnagrams("abcd"), 0)

  def test_cdcd(self):
    self.assertEqual(substringAnagrams("cdcd"), 5)

  def test_ifailuhkqq(self):
    self.assertEqual(substringAnagrams("ifailuhkqq"), 3)

  @unittest.skip("long - about 3 minutes")
  def test_big_0(self):
    s = "dbcfibibcheigfccacfegicigcefieeeeegcghggdheichgafhdigffgifidfbeaccadabecbdcgieaffbigffcecahafcafhcdg"
    self.assertEqual(substringAnagrams(s), 1464)

  @unittest.skip("long")
  def test_big_1(self):
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    self.assertEqual(substringAnagrams(s), 166650)

if __name__ == '__main__':
    unittest.main()