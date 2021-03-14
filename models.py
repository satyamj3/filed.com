import datetime as dt
from utils import get_connection


class Song:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.upload_time = dt.datetime.now()

    def save(self):
        """
        Saving the Song object to the Database
        """
        status = False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO song(name, duration, upload_time) values(?, ?, ?)",
                           (self.name, self.duration, self.upload_time))
            conn.commit()
            status = True
            print('Song created')
        except Exception as e:
            print(f"Exception {e}")
        finally:
            conn.close()
        return status

    def update(self, id):
        """
        update the Song data based on the id passed
        """
        status = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("update song set name = ?, duration = ? where id = ?",
                           (self.name, self.duration, id))
            conn.commit()
            status = True
            print('Podcast Updated')
        except Exception as e:
            print(f"Exception {e}")
        finally:
            conn.close()
        return status


class Podcast(Song):
    def __init__(self,
                 name='',
                 duration=0,
                 hostname='',
                 participants=[]
                 ):
        super().__init__(name, duration)
        self.host = hostname
        self.participants = ','.join(participants.split(','))

    def save(self):
        """
        Saving the Podcast object to the Database
        """
        status = False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO podcast(title, duration, upload_time, host, participants) values(?, ?, ?, ?, ?)",
                (self.name, self.duration, self.upload_time, self.host, self.participants))
            conn.commit()
            status = True
            print('Podcast created')
        except Exception as e:
            print(f"Exception {e}")
        finally:
            conn.close()
        return status

    def update(self, id):
        """
        update the Podcast data based on the id passed
        """
        status = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("update podcast set title = ?, duration = ?, host = ?, participants = ? where id = ?",
                           (self.name, self.duration, self.host, self.participants, id))
            conn.commit()
            status = True
            print('Podcast Updated')
        except Exception as e:
            print(f"Exception {e}")
        finally:
            conn.close()
        return status


class Audiobook(Song):
    def __init__(self,
                 name='',
                 duration=0,
                 author='',
                 narrator=''
                 ):
        super().__init__(name, duration)
        self.author = author
        self.narrator = narrator

    def save(self):
        """
        Saving the Audiobook object to the Database
        """
        status = False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO audiobook(title, duration, upload_time, author, narrator) values(?, ?, ?, ?, ?)",
                (self.name, self.duration, self.upload_time, self.author, self.narrator))
            conn.commit()
            status = True
        except Exception as e:
            print(f"Exception {e}")
        finally:
            conn.close()
        return status

    def update(self, id):
        """
        update the Podcast data based on the id passed
        """
        status = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("update audiobook set title = ?, duration = ?, author = ?, narrator = ? where id = ?",
                           (self.name, self.duration, self.author, self.narrator, id))
            conn.commit()
            status = True
            print('Audiobook Updated')
        except Exception as e:
            print(f"Exception {e}")
        finally:
            conn.close()
        return status


def delete_audiofile(audio_type, audio_id):
    """
    function to delete records based on the passed id
    param:
        audio_type: String - contins the audio file type which is also the table name in db
        aduio_id: id refers to the audiofile which helps in deleting the record
    """
    record_deleted = -1
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("delete from {} where id = {}".format(audio_type.lower(), audio_id))
        record_deleted = cursor.rowcount
        print('return', cursor.rowcount)
        conn.commit()
    except Exception as e:
        print(f"Error {e}")
    finally:
        conn.close()
    return record_deleted


def get_audiofile(audio_type, audio_id=None):
    data = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if audio_id is None:
            data = cursor.execute("SELECT * FROM {};".format(audio_type.lower())).fetchall()
        else:
            print("I got the audio id: ", audio_id)
            data = cursor.execute("SELECT * FROM {} where id = {};".format(audio_type.lower(), audio_id)).fetchall()
    except Exception as e:
        print(f"Exception {e}")
    finally:
        conn.close()
    return data
