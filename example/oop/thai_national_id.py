# %%
import re


# %%
class NationalID:
    """
    string_demo2 @property decorator
    ref: http://th.wikipedia.org/wiki/เลขประจำตัวประชาชนไทย
    """

    def __init__(self, national_id):
        self.national_id = self._remove_non_numeric(national_id)

    @property
    def citizen_type(self):
        return self.national_id[0]

    @property
    def regis(self):
        return self.national_id[1:5]

    @property
    def seq(self):
        return self.national_id[5:10]

    @property
    def sub_seq(self):
        return self.national_id[10:12]

    @property
    def check_digit(self):
        return self.national_id[-1]

    def is_valid(self):
        def calculate_check_digit(id_number: str) -> int:
            """ ตรวจตัวเลขตรวจสอบบัตรประชาชน
            :param id_number:
            :return:
            """
            x = (int(d) * i for d, i in zip(id_number[:12], range(13, 1, -1)))
            r = sum(x) % 11
            return 1 - r if r <= 1 else 11 - r

        return True if int(self.national_id[-1]) == calculate_check_digit(
            self.national_id) else False

    def _remove_non_numeric(self, s):
        return re.sub(r"[\D]", "", s)

    def pretty_format(self):
        return re.sub(r"(\d{1})(\d{4})(\d{5})(\d{2})(\d{1})", r"\1-\2-\3-\4-\5",
                      self.national_id)


# %%
if __name__ == '__main__':
    p = NationalID("1 1013 45673 82 2")
    print(p.national_id)
    print(p.pretty_format())
    print(p.citizen_type)
    print(p.regis)
    print(p.seq)
    print(p.sub_seq)
    print(p.check_digit)
    print(p.is_valid())
