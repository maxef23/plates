

def init_model(sqlDAO):
    from .NumberplateModel import Numberplate
    from .UserModel import User
    sqlDAO.create_all()
