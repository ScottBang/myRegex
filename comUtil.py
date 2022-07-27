import re


class comUtil:
    phoneReg = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')


    @classmethod
    def PhoneNumValidate(cls, value: str, groupNo: int = 0) -> str:
        mo = cls.phoneReg.search(value)
        rslt = ""

        if mo != None:
            rslt = mo.group(groupNo)

        return rslt
