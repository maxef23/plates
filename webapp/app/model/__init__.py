

def init_model(sqlDAO):
    from .NumberplateModel import Numberplate
    sqlDAO.create_all()
