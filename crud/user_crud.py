from models.user import User


def create_user(session, username):
    if not username or username.strip() == "":
        raise ValueError("username cannot be empty")

    user = User(username=username)
    session.add(user)
    session.commit()
    return user


def get_user_by_id(session, user_id):
    return session.query(User).get(user_id)


def get_user_by_username(session, username):
    return session.query(User).filter_by(username=username).first()


def update_user(session, user_id, new_username):
    user = session.query(User).get(user_id)
    if user:
        user.username = new_username
        session.commit()
    return user


def delete_user(session, user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()


def get_or_create_user(session, username):
    user = session.query(User).filter_by(username=username).first()

    if user:
        return user

    user = User(username=username)
    session.add(user)
    session.commit()
    return user