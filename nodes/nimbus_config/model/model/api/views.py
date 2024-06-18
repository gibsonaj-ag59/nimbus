from v_model.api import v_model_api
from flask import request
import re
import datetime
import calendar
import re
from sqlalchemy import and_, or_
from flask import request
import operator
from v_model.models import DataModel

@v_model_api.route(
        "/" + DataModel.__tablename__, 
        methods=['GET', 'POST']
        )
def query_device():
    if re.search(r'[-=&()]', request.query_string.decode()):
        result = DataModel.query.filter(
            *format_query(request)
            )
        json_string = [d.as_dict() for d in result.all()]
        return json_string
    else:
        result = DataModel.query.all()
        json_string = [d.as_dict() for d in result]
        return json_string

def format_query(req):
    _today = (_:=datetime.datetime.now()) - \
        datetime.timedelta(
            seconds=_.second,
            minutes=_.minute,
            hours=_.hour
            )
    _yester = _today - \
        datetime.timedelta(
            days=1,
            seconds=_today.second,
            minutes=_today.minute,
            hours=_today.hour
                        )
    _week = _today - \
        datetime.timedelta(
            weeks=1,
            seconds=_today.second,
            minutes=_today.minute,
            hours=_today.hour
            )
    _month = _today - datetime.timedelta(
        days=calendar.monthrange(_today.year,
                                    _today.month)[1],
        seconds=_today.second,
        minutes=_today.minute,
        hours=_today.hour
        )
    _year = _today - datetime.timedelta(
        days=sum(calendar.monthrange(
            _today.year, month
            )
            [1] for month in range(1, 13)
            ),
        seconds=_today.second,
        minutes=_today.minute,
        hours=_today.hour
    )
    encodings = {
                    'lt': getattr(operator, 'lt'),
                    'gt': getattr(operator, 'gt'),
                    'ge': getattr(operator, 'ge'),
                    'le': getattr(operator, 'le'),
                    'ne': getattr(operator, 'ne'),
                    'eq': getattr(operator, 'eq'),
                    '%2B': and_,
                    '%7C': or_,
                    'today': _today.date(),
                    'yester': _yester.date(),
                    'week': _week.date(),
                    'month': _month.date(),
                    'year': _year.date(),
                }
    query_string = req.query_string.decode()
    params = re.findall(r'[^-=&]+', query_string)
    f_params = []
    for p in params:
        f_params.append(encodings.get(p, p))
    oprs = []
    args = []
    cons = []
    stack = []
    for p in f_params:
        if callable(p):
            if len(p.__name__) > 2:
                cons.append(p)
            else:
                oprs.append(p)
        else:
            args.append(p)
    if len(cons) == 0:
        arg2 = args.pop()
        arg1 = args.pop()
        func = oprs.pop()
        stack.append(func(getattr(DataModel,
                                    arg1), arg2))
        return stack
    while len(cons) > 0:
        if len(stack) < 2:
            arg2 = args.pop()
            arg1 = args.pop()
            func = oprs.pop()
            stack.append(func(getattr(DataModel,
                                        arg1), arg2))
        if len(stack) == 2:
            arg2 = stack.pop()
            arg1 = stack.pop()
            cond = cons.pop()
            stack.append(cond(arg1, arg2))
    return stack