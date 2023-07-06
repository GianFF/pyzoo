# PyZoo

We are building a zoo inside a computer.
All animal species can talk to each other in a similar way. Specifically, they all implement a speak method, the output of which is the arbitrary input string interspersed with an "animal sound" that is particular to that type of animal.

For example, the lion's speak function behaves like so:

```py
> lion.speak("I'm a lion")
< "I'm roar a roar lion roar"
```

The tiger's speak function behaves similarly but with a different sound:

```py
> tiger.speak("Lions suck")
< "Lions grrr suck grrr"
```

When an animal speaks, if no phrase was given then it doesn't speaks.
For example, the tiger's speak function behaves like this:

```py
> tiger.speak("")
< ""
```

## Disclaimer

This project was created using Python3, to run the test execute `python3 -m unittest test_animal.py`

Technologies:
* Python 3
* FastAPI, run it with `uvicorn main:app --reload`
* SqlAlchemy
