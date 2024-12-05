from . import db
from flask_login import UserMixin

#make association table with baskets and books to use many to many relationship table
basket_textbook = db.Table('basket_textbook',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id',ondelete='CASCADE')),
    db.Column('product_id', db.Integer, db.ForeignKey('textbook.id'), nullable = False),
    db.Column('product_name',db.String(50), nullable=False),
    db.Column('price',db.Float,nullable=False),
    db.Column('quantity',db.Integer,nullable=False),
    db.Column('image_url', db.String(500), nullable=True),
    db.Column('stocks',db.Integer),
    db.Column('author',db.String(50), nullable=False)
    )

basket_science = db.Table('basket_science',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id',ondelete='CASCADE')),
    db.Column('product_id', db.Integer,db.ForeignKey('science.id'), nullable = False),
    db.Column('product_name',db.String(50), nullable=False),
    db.Column('price',db.Float,nullable=False),
    db.Column('quantity',db.Integer,nullable=False),
    db.Column('image_url', db.String(500), nullable=True),
    db.Column('stocks',db.Integer),
    db.Column('author',db.String(50), nullable=False)
    )

basket_novel = db.Table('basket_novel',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id',ondelete='CASCADE')),
    db.Column('product_id', db.Integer, db.ForeignKey('novel.id'), nullable = False),
    db.Column('product_name',db.String(50), nullable=False),
    db.Column('price',db.Float,nullable=False),
    db.Column('quantity',db.Integer,nullable=False),
    db.Column('image_url', db.String(500), nullable=True),
    db.Column('stocks',db.Integer),
    db.Column('author',db.String(50), nullable=False)

    )

basket_biography = db.Table('basket_biography',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id',ondelete='CASCADE')),
    db.Column('product_id', db.Integer,db.ForeignKey('biography.id'), nullable = False),
    db.Column('product_name',db.String(50), nullable=False),
    db.Column('price',db.Float,nullable=False),
    db.Column('quantity',db.Integer,nullable=False),
    db.Column('image_url', db.String(500), nullable=True),
    db.Column('stocks',db.Integer),
    db.Column('author',db.String(50), nullable=False)

    )

#Make Textbook model to contain data about textbook 

class Textbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500))
    name = db.Column(db.String(500),nullable=False)
    price = db.Column(db.Float, nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
 

#Make Science model to contain data about science book 
class Science(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500))
    name = db.Column(db.String(500),nullable=False)
    price = db.Column(db.Float, nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    author= db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


#Make Novel model to contain data about novel
class Novel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500))
    name = db.Column(db.String(500),nullable=False)
    price = db.Column(db.Float, nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    author= db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

#Make Biography model to contain data about biography 
class Biography(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500))
    name = db.Column(db.String(500),nullable=False)
    price = db.Column(db.Float, nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    author= db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

#Model for user detail

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(500),nullable=False, unique=True)
    password = db.Column(db.String(500), nullable = False)

#Model for Basket and make a relationship with books

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('baskets',lazy=True))
    textbook = db.relationship('Textbook', secondary = basket_textbook,primaryjoin="Basket.user_id == basket_textbook.c.user_id", 
                              secondaryjoin="basket_textbook.c.product_id == Textbook.id",backref='users')
    science = db.relationship('Science', secondary = basket_science, primaryjoin="Basket.user_id == basket_science.c.user_id", 
                              secondaryjoin="basket_science.c.product_id == Science.id", backref='users')
    novel = db.relationship('Novel', secondary = basket_novel,primaryjoin="Basket.user_id == basket_novel.c.user_id", 
                              secondaryjoin="basket_novel.c.product_id == Novel.id",backref='users')
    biography = db.relationship('Biography', secondary = basket_biography,primaryjoin="Basket.user_id == basket_biography.c.user_id", 
                              secondaryjoin="basket_biography.c.product_id == Biography.id",backref='users')

    """
    calculate total price
    bring a quantity data from association table then multiply with price, and add up 
    """

    def get_total_price(self):
        total = 0

        for item in self.textbook:
            association = db.session.query(basket_textbook).filter_by(user_id=self.user_id, product_id=item.id).first()
            total += item.price * association.quantity 

        for item in self.science:
            association = db.session.query(basket_science).filter_by(user_id=self.user_id, product_id=item.id).first()
            total += item.price * association.quantity 
        
        for item in self.novel:
            association = db.session.query(basket_novel).filter_by(user_id=self.user_id, product_id=item.id).first()
            total += item.price * association.quantity
        

        for item in self.biography:
            association = db.session.query(basket_biography).filter_by(user_id=self.user_id, product_id=item.id).first()
            total += item.price * association.quantity 
        
        return total