from app import create_app, db
from app.models import User , Pitch , Upvote, Downvote, Comment
from flask_script import Manager


manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch, Upvote = Upvote, Downvote = Downvote, Comment = Comment )
if __name__ == '__main__':
    manager.run()
