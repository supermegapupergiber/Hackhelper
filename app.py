
#### 3. **Backend (app.py)**

```python
from flask import Flask, jsonify, request
from models import User, Team
from services import ai_helper, rating_service

app = Flask(__name__)

# Список всех команд
@app.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.get_all_teams()
    return jsonify(teams)

# Профиль участника
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = User.get_user_by_id(user_id)
    return jsonify(user)

# Рейтинг команд и участников
@app.route('/ratings', methods=['GET'])
def get_ratings():
    ratings = rating_service.get_ratings()
    return jsonify(ratings)

# Поиск команд с помощью ИИ
@app.route('/search', methods=['POST'])
def search():
    data = request.json
    search_results = ai_helper.find_best_team(data['skills'], data['goals'])
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)
