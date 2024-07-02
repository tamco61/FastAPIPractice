

PRIVILEGES = Enum('admin', 'user')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    privileges = Column(PRIVILEGES)

    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    date = Column(Date)
    description = Column(String)
    link = Column(String, unique=True)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='books')