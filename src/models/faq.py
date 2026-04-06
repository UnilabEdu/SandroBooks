from src.models.base import BaseModel
from src.ext import db


class FrequentlyAskedQuestion(BaseModel):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.Integer, nullable=False, default=0)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<FAQ #{self.order_num}: {self.question[:50]}>"