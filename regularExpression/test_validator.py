val = "01012341234"

if val.startswith("010") and len(val) == 11:
    if val[:3] in ("010","011","016","017","018","019"):
        print("OK")



import re
#^시작0$끝
if re.match('^01[1-9]\d{6,7}$', val):
    print("matched")
else:
    print("invalid")

pattern = "^01[016789][1-9]\\d{6,7}$"
pattern = r"^01[016789][1-9]\d{6,7}$"  
#Python 에서는 \를 하나만 넣고 앞에 r을 붙여서 사용 가능 raw 사용 가능


#val = "01012341234" #11
#val = "0111231234"   #10
pattern = "01[016789][1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
pattern = "01[016789][1-9]\d\d\d\d\d\d"
pattern = "01[016789][1-9]\d{6}"

pattern = "01[016789][1-9][0-9][0-9][0-9][0-9][0-9][0-9]"

pattern = "01[016789][1-9]\d{6,7}"
#전화번호 나타내는 정규표현식

import re
def validate_phone_number(number):
    if not re.match(r'^01[016789][1-9]\d{6,7}$',number):
        return False
    return True

print(validate_phone_number('01012341234'))
print(validate_phone_number('01012321'))
print(validate_phone_number('01012341234a'))