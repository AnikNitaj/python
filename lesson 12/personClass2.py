from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self._weight = None
        self._height = None


        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than 0.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0.")

        if value > 3.0:
            value = value / 100.0
        self._height = value

    @abstractmethod
    def calculate_bmi(self) -> float:
        pass

    @abstractmethod
    def get_bmi_category(self) -> str:
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        print("\n" + "=" * 30)
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"Calculated BMI: {bmi:.2f}")
        print(f"Category: {self.get_bmi_category()}")
        print("=" * 30)


class Adult(Person):
    def calculate_bmi(self) -> float:
        return self.weight / (self.height ** 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi <= 24.9:
            return "Normal weight"
        elif bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self) -> float:
        return self.weight / (self.height ** 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()

        if bmi < 14.0:
            return "Underweight"
        elif bmi <= 22.0:
            return "Normal weight"
        elif bmi <= 25.0:
            return "Overweight"
        else:
            return "Obese"


if __name__ == "__main__":
    print("--- Personal BMI Calculator ---")

    try:
        user_name = input("Enter your name: ")
        user_age = int(input("Enter your age: "))
        user_weight = float(input("Enter your weight in kg: "))
        user_height = float(input("Enter your height (e.g., 1.75 or 175): "))


        if user_age >= 18:
            user = Adult(user_name, user_age, user_weight, user_height)
        else:
            print("\nProcessing as a Child/Teen profile...")
            user = Child(user_name, user_age, user_weight, user_height)

        user.print_info()

    except ValueError as e:
        print(f"\n[Error]: Invalid input. {e}")