from app import create_app, db
import app
from app.models import User , Pitch , Upvote, Downvote, Comment
from flask_script import Manager
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')


manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch, Upvote = Upvote, Downvote = Downvote, Comment = Comment )
if __name__ == '__main__':
    manager.run()
