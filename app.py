from flask import Flask
from flask import request
from flask import jsonify
from models import Song
from models import Podcast
from models import Audiobook
from models import delete_audiofile
from models import get_audiofile

app = Flask(__name__)
server_error = '500 internal server error'
bad_request = '400 bad request'
success = '200 OK'


@app.route('/Create/<string:audiofiletype>/', methods=['POST', 'GET'], strict_slashes=False)
def create_file(audiofiletype):
    audiofiletype = audiofiletype.lower()
    if audiofiletype == 'song':
        try:
            name = request.args.getlist('name')[0]
            duration = request.args.getlist('duration')[0]
            song = Song(name, duration)
            if not song.save():
                return server_error
            return success
        except IndexError as e:
            print(e)
            print(request.args)
            return bad_request
        except Exception as e:
            print(e)
            return server_error

    elif audiofiletype == 'podcast':
        try:
            name = request.args.getlist('name')[0]
            duration = request.args.getlist('duration')[0]
            host = request.args.getlist('host')[0]
            participants = request.args.getlist('participants')[0]
            podcast = Podcast(name, duration, host, participants)
            if not podcast.save():
                return server_error
            return success
        except IndexError as e:
            print(request.args)
            print(e)
            return bad_request
        except Exception as e:
            print(e)
            return server_error

    elif audiofiletype == 'audiobook':
        try:
            name = request.args.getlist('name')[0]
            duration = request.args.getlist('duration')[0]
            author = request.args.getlist('author')[0]
            narrator = request.args.getlist('narrator')[0]
            print(name, duration, author, narrator)
            audiobook = Audiobook(name, duration, author, narrator)
            if not audiobook.save():
                return server_error
            return success
        except IndexError as e:
            print(e)
            print(request.args)
            return bad_request
        except Exception as e:
            print(e)
            return server_error
    else:
        return bad_request


@app.route('/Update/<string:audiofiletype>/<int:audiofileid>', methods=['POST', 'GET'], strict_slashes=False)
def update_file(audiofiletype, audiofileid):
    audiofiletype = audiofiletype.lower()
    if audiofiletype == 'song':
        try:
            name = request.args.getlist('name')[0]
            duration = request.args.getlist('duration')[0]
            song = Song(name, duration)
            if not song.update(audiofileid):
                return server_error
            return success
        except IndexError as e:
            print(request.args)
            print(e)
            return bad_request
        except Exception as e:
            print(e)
            return server_error
    elif audiofiletype == 'podcast':
        try:
            name = request.args.getlist('name')[0]
            duration = request.args.getlist('duration')[0]
            host = request.args.getlist('host')[0]
            participants = request.args.getlist('participants')[0]
            podcast = Podcast(name, duration, host, participants)
            if not podcast.update(audiofileid):
                return server_error
            return success
        except IndexError as e:
            print('Index Error:', e)
            print(request.args)
            return bad_request
        except Exception as e:
            print('Server Error:', e)
            return server_error
    elif audiofiletype == 'audiobook':
        try:
            name = request.args.getlist('name')[0]
            duration = request.args.getlist('duration')[0]
            author = request.args.getlist('author')[0]
            narrator = request.args.getlist('narrator')[0]
            audiobook = Audiobook(name, duration, author, narrator)
            if not audiobook.update(audiofileid):
                return server_error
            return success
        except IndexError as e:
            print('Index Error:', e)
            print(request.args)
            return bad_request
        except Exception as e:
            print('Server Error:', e)
            return server_error
    else:
        return bad_request


@app.route('/Delete/<string:audiofiletype>/<int:fileid>', strict_slashes=False, methods=['GET', 'POST'])
def delete_file(audiofiletype, fileid):
    record_deleted = None
    record_deleted = delete_audiofile(audiofiletype, fileid)
    try:
        if record_deleted > 0:
            return success
        elif record_deleted == 0:
            return bad_request
    except Exception as e:
        print(e)
        return server_error


@app.route('/Get/<string:audiofiletype>/<int:fileid>/', strict_slashes=False, methods=['POST', 'GET'])
@app.route('/Get/<string:audiofiletype>/', strict_slashes=False, methods=['POST', 'GET'])
def get_file(audiofiletype, fileid=None):
    audiofiletype = audiofiletype.lower()
    if audiofiletype not in ['song', 'audiobook', 'podcast']:
        return bad_request
    else:
        data = get_audiofile(audiofiletype, fileid)
        if data is None:
            return server_error
        else:
            return jsonify(data)


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
