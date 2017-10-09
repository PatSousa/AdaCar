import os
import sys
import transaction
import json
import random

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )

from ..models import PartType, Category,Part


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Get values from files
    here = os.path.abspath(os.path.dirname(__file__))
    category = json.load(open(os.path.join(here, '../mockdata/category.json'), 'r'))
    part = json.load(open(os.path.join(here, '../mockdata/part.json'), 'r'))
    type = json.load(open(os.path.join(here, '../mockdata/part_type.json'), 'r'))

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        with dbsession.no_autoflush:

        # Insert a Person in the person table
            for elem in category:
                new_category = Category(
                    category_id=elem['category_id'],
                    category_name=elem['category_name'])
                dbsession.add(new_category)
                dbsession.flush()
                transaction.commit()

            for elem in type:
                cat_id = random.randint(1,10)
                part_type_category = dbsession.query(Category).filter_by(category_id=cat_id).first()
                if part_type_category:
                    new_type = PartType(
                        part_type_id=elem['part_type_id'],
                        part_type_name=elem['part_type_name'],
                        part_type_description=elem['part_type_description'],
                        part_type_value=elem['part_type_value'],
                        part_type_image_url=elem['part_type_image_url'],
                        part_type_category=part_type_category.category_id)
                    dbsession.add(new_type)
                    dbsession.flush()
                    transaction.commit()

            for index, elem in enumerate(part):
                part_type = dbsession.query(PartType).filter_by(part_type_id=elem['part_type']).first()
                category = dbsession.query(Category).filter_by(category_id=elem['part_category']).first()
                if part_type and category:
                    new_part = Part(
                        part_uid=elem['part_id'],
                        part_type=part_type.part_type_id,
                        part_category=category.category_id)
                    dbsession.add(new_part)
                    dbsession.flush()
                    transaction.commit()

                    # model = Part(name='one', value=1)
                    # dbsession.add(model)
