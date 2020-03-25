import factory
import datetime
import factory.fuzzy as fuzzy
import random
from api import db
from api.todos.models import TodoModel


class TodoFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = TodoModel
        sqlalchemy_session = db.session

    title = factory.Faker('text')
    description = factory.Faker('sentence')
    from_date = fuzzy.FuzzyDate(datetime.date(2008, 1, 1))
    to_date = fuzzy.FuzzyDate(datetime.date(2018, 1, 1))
    completed = factory.LazyFunction(lambda: random.choice([True, False]))
