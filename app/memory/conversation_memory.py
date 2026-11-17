
from app.database.database import SessionLocal
from app.database.models import Message


class ConversationMemory:

    def __init__(self, session_id="default", max_messages=20):
        self.session_id = session_id
        self.max_messages = max_messages

    def add_message(self, role, content):

        db = SessionLocal()

        try:
            message = Message(
                session_id=self.session_id,
                role=role,
                content=content
            )

            db.add(message)
            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    def get_history(self):

        db = SessionLocal()

        try:
            messages = (
                db.query(Message)
                .filter(Message.session_id == self.session_id)
                .order_by(Message.created_at.desc(), Message.id.desc())
                .limit(self.max_messages)
                .all()
            )

            messages.reverse()

            return [
                {
                    "role": message.role,
                    "content": message.content
                }
                for message in messages
            ]

        finally:
            db.close()

    def clear_history(self):

        db = SessionLocal()

        try:
            db.query(Message).filter(
                Message.session_id == self.session_id
            ).delete()

            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()
