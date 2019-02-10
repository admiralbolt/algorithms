import glob
import os
import pickle

def generate_primes(n, file_prefix="primes"):
  """Generates all primes up to a number n and saves them to primes_%n%_%d%.pickle

  %d% is calculated as the number of primes written.
  The primes are generated using the sieve of eratosthenes method.
  """
  is_prime = [False, False] + [True] * (n - 1)
  prime = 2
  # We only need to iterate up to the sqrt(n)
  while prime * prime < n:
    if is_prime[prime]:
      # Mark off all multiples of the prime as not prime.
      for i in range(prime * 2, n + 1, prime):
        is_prime[i] = False
    prime += 1
  primes = [p for p in range(2, n + 1) if is_prime[p]]
  file_name = "%s_%s_%s.pickle" % (file_prefix, n, len(primes))
  file_path = os.path.join(os.path.dirname(__file__), file_name)
  with open(file_path, "wb") as wh:
    pickle.dump((is_prime, primes), wh)

def load_primes(max_number = None, number_of_primes = None, file_prefix="primes"):
  """Loads pickled primes. Returns a tuple of (is_prime, primes).

  is_prime is a list of booleans that correspond to if a particular number is prime.
  primes is a list of all the prime numbers.

  If max_number and number_of_primes are not specified, loads the largest amount
  of primes available. Otherwise, if max_number OR number_of_primes is specified
  a particular file is attempted to be loaded instead.

  file_prefix is used for calculating the pickled files to load from.
  """
  file_glob = os.path.join(os.path.dirname(__file__), "%s*.pickle" % file_prefix)
  pickled_primes = glob.glob(file_glob)
  max_primes = 0
  max_prime_file = ""
  for file_name in pickled_primes:
    file_prefix, file_max, file_number = os.path.splitext(file_name)[0].split("_")
    if int(file_max) > max_primes:
      max_primes = int(file_max)
      max_prime_file = file_name
    if max_number is not None or number_of_primes is not None:
      if int(file_max) == max_number or int(file_number) == number_of_primes:
        with open(file_name, "rb") as rh:
          return pickle.load(rh)
        return file_name
  if max_number is not None or number_of_primes is not None:
    print("Could not find a saved prime file with max_number: %s, or "
          "number_of_primes: %s. Returning max instead." % (max_number, number_of_primes))
  with open(max_prime_file, "rb") as rh:
    return pickle.load(rh)
