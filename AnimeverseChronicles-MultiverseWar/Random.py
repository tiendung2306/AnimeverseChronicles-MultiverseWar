import os

class Random():
    def get_truly_random_seed_through_os(self) -> int:
            """
            Usually the best random sample you could get in any programming language is generated through the operating system. 
            In Python, you can use the os module.

            source: https://stackoverflow.com/questions/57416925/best-practices-for-generating-a-random-seeds-to-seed-pytorch/57416967#57416967
            """
            RAND_SIZE = 4
            random_data = os.urandom(
                RAND_SIZE
            )  # Return a string of size random bytes suitable for cryptographic use.
            random_seed: int = int.from_bytes(random_data, byteorder="big")
            return int(random_seed)

    def get_different_pseudo_random_seed_every_time_using_time(self) -> int:
        import random
        import time

        # random.seed(int(time.time()))
        seed: int = int(time.time())
        return seed