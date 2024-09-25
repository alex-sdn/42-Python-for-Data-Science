
class calculator:
    """
    Class with static methods to perform calculations on two vectors
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the dot product of two lists of floats"""
        dot = 0
        for i in range(0, len(V1)):
            dot += V1[i] * V2[i]

        print(f"Dot product is: {dot}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the sum of two lists of floats"""
        vec = []
        for i in range(0, len(V1)):
            vec.append(float(V1[i] + V2[i]))

        print(f"Add Vector is: {vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the subtraction of two lists of floats"""
        vec = []
        for i in range(0, len(V1)):
            vec.append(float(V1[i] - V2[i]))

        print(f"Sous Vector is: {vec}")
