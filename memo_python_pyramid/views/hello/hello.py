from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='hello', renderer='memo_python_pyramid:templates/hello.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'memo_python_pyramid'}
    
