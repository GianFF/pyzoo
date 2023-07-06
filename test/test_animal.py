import unittest
import src.domain.animal as animal

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.kitten = animal.Animal('Cat', 'miau')

    def test_an_animal_has_a_specie(self):
        self.assertEqual(self.kitten.specie, 'Cat')

    def test_an_animal_has_an_animal_sound(self):
        self.assertEqual(self.kitten.animal_sound, 'miau')

    # test_an_animal_can_speak
    def test_an_animal_can_speak__given_a_phrase_they_can_interprese_it_with_their_animal_sound(self):
      self.assertEqual(self.kitten.speak('Hello world'), 'Hello miau world miau')

    def test_an_animal_can_speak__given_an_empty_phrase_they_do_not_say_anything(self):
      self.assertEqual(self.kitten.speak(''), '')
    
    def test_an_animal_can_speak__given_no_phrase_it_throws(self):
      with self.assertRaises(TypeError):
            self.kitten.speak()

    def test_an_animal_can_speak__given_a_blank_phrase_they_repeat_their_animal_sound(self):
      self.assertEqual(self.kitten.speak(' '), ' miau  miau')
    
if __name__ == '__main__':
    unittest.main()