from database import engine, SessionLocal, Base

from models.user import User
from models.profile import Profile
from models.post import Post
from models.tag import Tag

from crud.user_crud import get_or_create_user


# создать таблицы
Base.metadata.create_all(bind=engine)

session = SessionLocal()

# -----------------------
# 👤 USERS
# -----------------------
user1 = get_or_create_user(session, "john")
user2 = get_or_create_user(session, "alice")

# -----------------------
# 🪪 PROFILES (1:1)
# -----------------------
profile1 = Profile(bio="I love coding", user=user1)
profile2 = Profile(bio="Designer", user=user2)

session.add_all([profile1, profile2])

# -----------------------
# 📝 POSTS (1:N)
# -----------------------
post1 = Post(title="First Post", user=user1)
post2 = Post(title="Second Post", user=user1)
post3 = Post(title="Alice Post", user=user2)

session.add_all([post1, post2, post3])

# -----------------------
# 🏷 TAGS (N:N) SAFE VERSION
# -----------------------
def get_or_create_tag(session, name):
    tag = session.query(Tag).filter_by(name=name).first()

    if tag:
        return tag

    tag = Tag(name=name)
    session.add(tag)
    session.commit()
    return tag


tag1 = get_or_create_tag(session, "python")
tag2 = get_or_create_tag(session, "life")

post1.tags.append(tag1)
post1.tags.append(tag2)
post2.tags.append(tag1)

session.commit()

# -----------------------
# 🔍 QUERIES
# -----------------------
print("\n--- USER BY ID ---")
print(get_or_create_user(session, "john"))

print("\n--- USER POSTS ---")
user = get_or_create_user(session, "john")
for post in user.posts:
    print(post.title)

print("\n--- POSTS BY TAG python ---")
tag = session.query(Tag).filter_by(name="python").first()
for post in tag.posts:
    print(post.title)

# -----------------------
# 🔄 UPDATE
# -----------------------
user1.username = "john_updated"
session.commit()

# -----------------------
# 🗑 DELETE EXAMPLE
# -----------------------
session.delete(user2)
session.commit()

print("\nDONE")