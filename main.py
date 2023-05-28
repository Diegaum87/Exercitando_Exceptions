from erros.div_by_zero import div_by_zero
from erros.misterious_error import misterious_error
from erros.unexisting_index import unexisting_index
from erros.unexisting_key import unexisting_key


if __name__ == "__main__":
    try:
        div_by_zero()
    except ZeroDivisionError:
        print('ZeroDivisionError tratado!')

    try:
        unexisting_key()
    except KeyError:
        print('KeyError tratado!')

    try:
        unexisting_index()
    except IndexError:
        print('IndexError tratado!')

    try:
        misterious_error()
    except AttributeError:
        print('AttributeError tratado!')