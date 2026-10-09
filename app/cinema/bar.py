from app.people.customer import Customer as ct


class CinemaBar:
    @staticmethod
    def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
        print(f"Cinema bar sold {ct.products} to {ct.name}.")
