from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, FloatField
from wtforms.validators import DataRequired, ValidationError

class PieForm(FlaskForm):
    quantity = IntegerField('quantity', validators=[DataRequired()])
    # order_id = IntegerField('order_id')
    menu_item = BooleanField('menu_item')
    pie_img = StringField('pie_img')
    price = FloatField('price', validators=[DataRequired()])
    bake = StringField('bake', validators=[DataRequired()])
    cut = StringField('cut', validators=[DataRequired()])
    size = StringField('size', validators=[DataRequired()])
    style = StringField('style', validators=[DataRequired()])
    seasoning = BooleanField('seasoning', validators=[DataRequired()])
    cheese = IntegerField('cheese')
    robust_inspired_tomato_sauce = IntegerField('robust_inspired_tomato_sauce')
    hearty_marinara_sauce = IntegerField('hearty_marinara_sauce')
    honey_bbq_sauce = IntegerField('honey_bbq_sauce')
    garlic_parmesan_sauce = IntegerField('garlic_parmesan_sauce')
    alfredo_sauce = IntegerField('alfredo_sauce')
    ranch = IntegerField('ranch')
    ham = IntegerField('ham')
    italian_sausage = IntegerField('italian_sausage')
    beef = IntegerField('beef')
    premium_chicken = IntegerField('premium_chicken')
    bacon = IntegerField('bacon')
    salami = IntegerField('salami')
    philly_steak = IntegerField('philly_steak')
    pepperoni = IntegerField('pepperoni')
    hot_buffalo_sauce = IntegerField('hot_buffalo_sauce')
    jalapeno_pepper = IntegerField('jalapeno_pepper')
    onion = IntegerField('onion')
    banana_pepper = IntegerField('banana_pepper')
    diced_tomato = IntegerField('diced_tomato')
    black_olive = IntegerField('black_olive')
    mushroom = IntegerField('mushroom')
    pineapple = IntegerField('pineapple')
    cheddar_cheese = IntegerField('cheddar_cheese')
    green_pepper = IntegerField('green_pepper')
    spinach = IntegerField('spinach')
    roasted_red_pepper = IntegerField('roasted_red_pepper')
    feta_cheese = IntegerField('feta_cheese')
    shredded_parmesan_asiago = IntegerField('shredded_parmesan_asiago')
    american_cheese = IntegerField('american_cheese')
    shredded_provolone_cheese = IntegerField('shredded_provolone_cheese')
