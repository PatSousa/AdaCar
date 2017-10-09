from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base

class Category(Base):
    """Model defining a product category"""
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(Text)


class PartType(Base):
    """Model defining a product type"""
    __tablename__ = 'part_types'
    part_type_id = Column(Integer, primary_key=True)
    part_type_name = Column(Text)
    part_type_description = Column(Text)
    part_type_value = Column(Integer)
    part_type_image_url = Column(Text)
    part_type_category = Column(
        Integer, ForeignKey("categories.category_id", ondelete="CASCADE"), nullable=False)


    def to_json(self):
        """ Short serializer of the product type """
        return dict(part_type_id=self.part_type_id,
                    part_type_name=self.part_type_name,
                    part_type_description=self.part_type_description,
                    part_type_value = self.part_type_value,
                    part_type_image_url = self.part_type_image_url,
                    part_type_category = self.part_type_category,
                    )

class Part(Base):
    """
    Model defining a product.
    FK to part_type, category and also order.
    If a product already belongs to an order, can't be picked by another order.
    This enables some sort of product stock.
    """
    __tablename__ = 'parts'
    part_id = Column(Integer, primary_key=True)
    part_uid = Column(Text)

    order = Column(
        Integer, ForeignKey("orders.order_id"), nullable=True
    )

    part_type = Column(
        Integer, ForeignKey("part_types.part_type_id", ondelete="CASCADE"), nullable=False
    )
    part_category = Column(
        Integer, ForeignKey("categories.category_id", ondelete="CASCADE"), nullable=False
    )

    def to_json(self):
        """ Short serializer of the product type """
        return dict(part_id=self.part_id,
                    part_uid=self.part_uid,
                    order=self.order,
                    part_type = self.part_type,
                    part_category = self.part_category,
                    )



