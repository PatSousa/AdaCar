from sqlalchemy import (
    Column,
    DateTime,
    Integer,
)

from .meta import Base


class Order(Base):
    """
    Model describing an order.
    When a delivery date is set, order is finalized
    """
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    delivery_date = Column(DateTime)

    def to_json(self):
        return dict(order_id=self.order_id,
                    delivery_date=self.delivery_date,)