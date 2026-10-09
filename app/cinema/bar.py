from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def cinema_visit(customers: list[Customer], hall_number: int, cleaner: str, movie: str):
        print(f"Cinema bar sold {customers.food} to {customers.name}.")
