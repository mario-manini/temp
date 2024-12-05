from flask import render_template,flash,redirect,url_for, request,session, flash
from app import app,db, bcrypt
from flask_login import login_user, LoginManager, login_required, login_user, current_user, logout_user
from .models import Textbook, Novel, Biography, Science, Basket, basket_textbook, basket_science, basket_novel, basket_biography, User
from .forms import LoginForm, CreateAccountForm


login_manager = LoginManager()  #inital login
login_manager.init_app(app)
login_manager.login_view = "login"  

@app.route('/')                 #load to start page
def home():
    return render_template('start.html')

@app.route('/add')              # when start button is clicked add all book data to databse manually
def add():                      # user can't go to start page again                 
    #add textbook data to database
    textbook = Textbook.query.all()
    textbook1 = Textbook(image_url="https://m.media-amazon.com/images/I/61Mw06x2XcL._SL1500_.jpg",name="Introduction to Algorithms",price=40.00,stocks=10, author=" Thomas H. Cormen",quantity = 1)
    textbook2 = Textbook(image_url="https://m.media-amazon.com/images/I/712Qlq3iHcL._SL1500_.jpg",name="Effective C++",price=36.67,stocks=10,author="Scott Myers", quantity = 1)
    textbook3 = Textbook(image_url="https://m.media-amazon.com/images/I/51EyaJeebHL._SL1056_.jpg",name="The C Programming Language",price=40.41,stocks=10,author="Brian Kernighan",quantity = 1)
    textbook4 = Textbook(image_url="https://m.media-amazon.com/images/I/51E2055ZGUL._SL1000_.jpg",name="Clean Code",price=38.63,stocks=10,author="Robert Martin", quantity = 1)

    db.session.add(textbook1)
    db.session.add(textbook2)
    db.session.add(textbook3)
    db.session.add(textbook4)
    db.session.commit() #commit change


    #add science data to database
    science1 = Science(image_url="https://m.media-amazon.com/images/I/61CXvkfdXlL._SL1500_.jpg",
                     name="The Selfish Gene", price=9.99, stocks=10,author="Richard Dawkins", quantity = 1)
    science2 = Science(image_url="https://upload.wikimedia.org/wikipedia/en/9/91/Cosmos_book.gif",
                     name="Cosmos", price=32.00, stocks=10, author="Carl Sagan", quantity = 1)
    science3 = Science(image_url="https://m.media-amazon.com/images/I/71RG9cuteML._SL1500_.jpg",
                     name="Silent Spring", price=19.99, stocks=10, author="Rachel Carson", quantity = 1)
    science4 = Science(image_url="https://m.media-amazon.com/images/I/71++XzvBcbL._SL1500_.jpg",
                     name="Brief Answers to the Big Questions", price=8.81, stocks=10,author="Stephen Hawking", quantity = 1)

    
    db.session.add(science1)
    db.session.add(science2)
    db.session.add(science3)
    db.session.add(science4)
    db.session.commit() #commit change

    novel1 = Novel(image_url="https://m.media-amazon.com/images/I/61xGLpWLIKL._SL1500_.jpg",
                     name="1984", price=6.62, stocks=10, author="George Orwell", quantity = 1)
    novel2 = Novel(image_url="https://m.media-amazon.com/images/I/91yg5rniqwL._SL1500_.jpg",
                     name="The Great Gatsby", price=7.29, stocks=10, author="F.Scott Fitzgerald", quantity = 1)
    novel3 = Novel(image_url="https://m.media-amazon.com/images/I/81gepf1eMqL._SL1500_.jpg",
                     name="To Kill A Mockingbird", price=8.35, stocks=10, author="Harper Lee", quantity = 1)
    novel4 = Novel(image_url="https://m.media-amazon.com/images/I/41NFqPZ0itL._SL1400_.jpg",
                     name="The Handmaid's Tale", price=8.30, stocks=10, author="Magaret Atwood", quantity = 1)

    db.session.add(novel1)
    db.session.add(novel2)
    db.session.add(novel3)
    db.session.add(novel4)
    db.session.commit()

    biography1 = Biography(image_url="https://m.media-amazon.com/images/I/717LHuYp7uL._SL1500_.jpg",
                     name="Shoedog", price=8.75, stocks=10, author="Phil Knight",quantity = 1)
    biography2 = Biography(image_url="https://m.media-amazon.com/images/I/41RCzknAdzL.jpg",
                     name="Steve Jobs", price=16.27, stocks=10, author="Walter Isaccson",quantity = 1)
    biography3 = Biography(image_url="https://m.media-amazon.com/images/I/81rJjvTQfgL._SL1500_.jpg",
                     name="Elon Musk", price=14.50, stocks=10, author="Walter Isaccson",quantity = 1)
    biography4 = Biography(image_url="https://m.media-amazon.com/images/I/81npSx097IL._SL1500_.jpg",
                     name="American Prometheus", price=11.45, stocks=10, author=" Kai Bird",quantity = 1)


    db.session.add(biography1)
    db.session.add(biography2)
    db.session.add(biography3)
    db.session.add(biography4)
    db.session.commit()

    return render_template('home.html')

@app.route('/home')                                                                     #load homepage
def home2():
    return render_template('home.html')

@app.route('/textbook',methods=['GET'])                                                 #load textbook data to display
def textbook():
    textbook = Textbook.query.all()

    return render_template('Textbook.html', textbook=textbook)
    

@app.route('/science',methods=['GET'])                                                  #load science book data to display
def science():
    science = Science.query.all()

    return render_template('Science.html', science=science)


@app.route('/novel',methods=['GET'])                                                    #load novel data to display
def novel():
    novel = Novel.query.all()

    return render_template('Novel.html',novel=novel)


@app.route('/biography',methods=['GET'])                                                #load biography data to display
def biography():
    biography = Biography.query.all()

    return render_template('Biography.html',biography=biography)

@app.route('/error')                                                                    #load error template when it's out of stock
def error():
    return render_template('error.html')

"""
login function
get user data with form
if data is valid from database, let user login with flask-login
"""

@app.route('/login',methods=['GET','POST'])                                                 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()                
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home2'))

    return render_template('login.html',form = form)

#log out user by flask-login

@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

"""
get user details through form
save it to database to login
"""

@app.route('/register',methods=["GET", "POST"])
def create():
    form = CreateAccountForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('create.html',form=form)

"""
To show basket,
get all the product data from association table by user_id
and send it to html
"""

@app.route('/user/<int:user_id>/basket', methods=['GET'])
@login_required
def view_basket(user_id):

    basket = Basket.query.filter_by(user_id=user_id).first()

    user = current_user
    user_id = user.id

    if not basket:                              #if there isn't basket make new basket
        basket = Basket(user_id=user_id)
        db.session.add(basket)
        db.session.commit()

    textbook = basket.textbook                  #get data from association table
    science = basket.science
    novel = basket.novel
    biography = basket.biography

    basket_textbook_items = db.session.query(basket_textbook).filter_by(user_id=user_id).all()
    basket_novel_items = db.session.query(basket_novel).filter_by(user_id=user_id).all()
    basket_biography_items = db.session.query(basket_biography).filter_by(user_id=user_id).all()
    basket_science_items = db.session.query(basket_science).filter_by(user_id=user_id).all()

    textbooks_in_basket = []                    #assign data to new list
    for item in basket_textbook_items:
        textbooks_in_basket.append({
            'user_id': item.user_id,
            'product_name': item.product_name,
            'product_id': item.product_id,
            'author': item.author,
            'price': item.price,
            'quantity': item.quantity,
            'image_url': item.image_url
        })

    novels_in_basket = []
    for item in basket_novel_items:
        novels_in_basket.append({
            'user_id': item.user_id,
            'product_name': item.product_name,
            'product_id': item.product_id,
            'author': item.author,
            'price': item.price,
            'quantity': item.quantity,
            'image_url': item.image_url
        })

    biographies_in_basket = []
    for item in basket_biography_items:
        biographies_in_basket.append({
            'user_id': item.user_id,
            'product_name': item.product_name,
            'product_id': item.product_id,
            'author': item.author,
            'price': item.price,
            'quantity': item.quantity,
            'image_url': item.image_url
        })

    science_in_basket = []
    for item in basket_science_items:
        science_in_basket.append({
            'user_id': item.user_id,
            'product_name': item.product_name,
            'product_id': item.product_id,
            'author': item.author,
            'price': item.price,
            'quantity': item.quantity,
            'image_url': item.image_url
        })

    total_price = round(basket.get_total_price(),2)     #get total price with round up 2decimal

    return render_template(
        'basket.html',
        textbook=textbook,
        science=science,
        novel=novel,
        biography=biography,
        user=current_user,
        total_price=total_price,
        textbooks_in_basket=textbooks_in_basket,
        novels_in_basket=novels_in_basket,
        biographies_in_basket=biographies_in_basket,
        science_in_basket=science_in_basket
    )

#load textbook data by id

@app.route('/textbook/<int:textbook_id>')
def view_textbook(textbook_id):
    textbook = Textbook.query.get_or_404(textbook_id)

    return render_template('textbook_view.html',textbook = textbook)

#load science book data by id

@app.route('/science/<int:science_id>')
def view_science(science_id):
    science = Science.query.get_or_404(science_id)

    return render_template('science_view.html',science=science)

#load novel data by id

@app.route('/novel/<int:novel_id>')
def view_novel(novel_id):
    novel = Novel.query.get_or_404(novel_id)

    return render_template('novel_view.html',novel=novel)

#load biography data by id

@app.route('/biography/<int:biography_id>')
def view_biography(biography_id):
    biography = Biography.query.get_or_404(biography_id)

    return render_template('biography_view.html',biography=biography)

"""
To add data,
add button in html send product_id and product_type
query the data which is from id an type
if stock is more than 0,
add the product to basket database and update quantity (if product is in the basket just add one more quantity)
commit all the change

"""
@app.route('/add', methods=['POST'])
@login_required
def add_to_basket():
    product_id = request.form.get('product_id')
    product_type = request.form.get('product_type')

    if product_type == 'textbook':                          #If product_type sends textbook
        product = Textbook.query.get(product_id)            #Query data from Textbook 
        table = basket_textbook
    elif product_type == 'science':                         #If product_type sends textbook
        product = Science.query.get(product_id)             #Query data from science
        table = basket_science
    elif product_type == 'novel':                           #If product_type sends novel
        product = Novel.query.get(product_id)               #Query data from science
        table = basket_novel
    elif product_type == 'biography':                       #If product_type sends biography 
        product = Biography.query.get(product_id)           #Query data from science
        table = basket_biography
    else:
        return "Product type not recognized", 400

    if not product:
        return "Product not found", 404

    try:
        if product.stocks > 0:          #if product is more than 0 -1 from stock and just add product
            product.stocks -= 1
            db.session.add(product)
            db.session.commit()

            db.session.refresh(product)


            existing_item = db.session.query(table).filter_by(user_id=current_user.id, product_id=product.id).first()

            if existing_item:           #if there is same prodcut then add + 1 for quality
                db.session.query(table).filter_by(user_id=current_user.id, product_id=product.id).update({
                    'quantity': existing_item.quantity + 1
                })
            else:
                new_item = table.insert().values(   #get data from association table and add it
                    user_id=current_user.id,
                    product_id=product.id,
                    product_name=product.name,
                    price=product.price,
                    quantity=1,
                    image_url=product.image_url,
                    stocks=product.stocks,
                    author=product.author
                )
                db.session.execute(new_item)

            db.session.commit()
        else:
            return render_template('error.html')
    except Exception as e:
        db.session.rollback()  # Roll back the transaction in case of errors
        print(f"Error: {e}")
        return "An error occurred", 500

    return render_template('added_basket.html', userid=current_user.id)

"""
To delete data,
when x button is clicked get data from association table which is related
delete related data
and update stocks(add quantity to stocks)

"""

@app.route('/delete_product', methods=['POST'])
def delete_product():
    product_id = request.form.get('product_id')
    user_id = request.form.get('user_id')
    product_type = request.form.get('product_type')

    if not product_id or not user_id or not product_type:
        flash('Invalid request', 'error')
        return redirect(url_for('view_basket', user_id=user_id))

    if product_type == 'textbook': #if it is textbook, query textbook data with user_id and product_id
        basket_item = db.session.query(basket_textbook).filter_by(user_id=user_id, product_id=product_id).first()
        db.session.query(basket_textbook).filter_by(user_id=user_id, product_id=product_id).delete()


        product = Textbook.query.get(product_id)    #add stocks
        if product:
            product.stocks += basket_item.quantity

    elif product_type == 'science': #if it is science, query science data with user_id and product id
        basket_item = db.session.query(basket_science).filter_by(user_id=user_id, product_id=product_id).first()
        db.session.query(basket_science).filter_by(user_id=user_id, product_id=product_id).delete()

        product = Science.query.get(product_id)
        if product:
            product.stocks += basket_item.quantity

    elif product_type == 'novel':   #if it is novel, query novel data with user_id and product id
        basket_item = db.session.query(basket_novel).filter_by(user_id=user_id, product_id=product_id).first()
        db.session.query(basket_novel).filter_by(user_id=user_id, product_id=product_id).delete()

        product = Novel.query.get(product_id)   #add stocks
        if product:
            product.stocks += basket_item.quantity

    elif product_type == 'biography':   #if it is biography, query biography data with user_id and product id
        basket_item = db.session.query(basket_biography).filter_by(user_id=user_id, product_id=product_id).first()
        db.session.query(basket_biography).filter_by(user_id=user_id, product_id=product_id).delete()

        product = Biography.query.get(product_id)
        if product:
            product.stocks += basket_item.quantity  #add stocks

    db.session.commit()

    return redirect(url_for('view_basket', user_id=user_id))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))