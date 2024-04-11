from flask import Flask, jsonify, request
from .models import db, User, Story, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/api/stories/<int:story_id>/comments', methods=['GET'])
def get_comments(story_id):
    comments = Comment.query.filter_by(story_id=story_id).all()
    return jsonify([comment.serialize() for comment in comments])

# Other routes for fetching stories, user profiles, etc.

if __name__ == '__main__':
    app.run(debug=True)
