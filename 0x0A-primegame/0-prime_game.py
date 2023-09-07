#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
  """
  Determines the winner of the prime game.

  Args:
    x: The number of rounds.
    nums: An array of the numbers in each round.

  Returns:
    The name of the player that won the most rounds, or None if the winner cannot be determined.
  """

  scores = {"Maria": 0, "Ben": 0}
  for i in range(x):
    current_nums = nums[i]
    winner = findWinner(current_nums)
    scores[winner] += 1

  most_wins = max(scores.values())
  winners = [key for key, value in scores.items() if value == most_wins]

  if len(winners) == 1:
    return winners[0]
  else:
    return None

def findWinner(nums):
  """
  Determines the winner of a single round of the prime game.

  Args:
    nums: The numbers in the round.

  Returns:
    The name of the player that won the round, or None if the winner cannot be determined.
  """

  if len(nums) == 1:
    return "Ben"

  primes = [prime for prime in nums if isPrime(prime)]
  if len(primes) == 0:
    return "Maria"

  next_move = findBestMove(primes)
  if next_move is None:
    return "Maria"

  return "Ben"

def isPrime(num):
  """
  Determines if a number is prime.

  Args:
    num: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if num < 2:
    return False

  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False

  return True

def findBestMove(primes):
  """
  Finds the best move for a player in a round of the prime game.

  Args:
    primes: The prime numbers in the round.

  Returns:
    The index of the best move, or None if there is no best move.
  """

  best_move = None
  best_score = -float("inf")

  for i in range(len(primes)):
    new_primes = primes[:i] + primes[i + 1:]
    score = getScore(new_primes)

    if score > best_score:
      best_move = i
      best_score = score

  return best_move

def getScore(primes):
  """
  Gets the score of a set of prime numbers.

  Args:
    primes: The prime numbers to get the score for.

  Returns:
    The score of the set of prime numbers.
  """

  score = len(primes)

  for prime in primes:
    for i in range(prime, len(primes)):
      if primes[i] % prime == 0:
        score -= 1
        break

  return score
