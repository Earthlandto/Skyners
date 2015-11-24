import re

def checkio(data):

    if len(data) < 10 :
        return False

    hasUpper = re.match('[A-Z]+', data) is None
    hasLower = re.match('[a-z]+', data) is None
    hasNumber = re.match('[0-9', data) is None

    return hasNumber and hasLower and hasUpper



if __name__ == '__main__':
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
