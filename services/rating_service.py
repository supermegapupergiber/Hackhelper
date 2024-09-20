class RatingService:
    def __init__(self):
        pass

    def get_ratings(self):
        # Пример данных для демонстрации
        ratings = {
            'teams': [
                {'name': 'Team Alpha', 'rating': 9.5},
                {'name': 'Team Bravo', 'rating': 8.7},
                {'name': 'Team Gamma', 'rating': 9.2}
            ],
            'users': [
                {'name': 'User 1', 'rating': 9.8},
                {'name': 'User 2', 'rating': 9.0},
                {'name': 'User 3', 'rating': 8.5}
            ]
        }
        return ratings

rating_service = RatingService()
