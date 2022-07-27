
from unittest import TestCase
import re

from comUtil import comUtil


class TestPhoneNumValidate(TestCase):

    def test_phoneNumValidate(self):
        """
        전화번호 패턴 테스트
            : 숫자를 나타내는 '\d' 기호.
        """
        # given
        phoneNum_01 = "010-5592-6688"
        phoneNum_02 = "My number is 010-5592-6688."
        phoneNum_03 = "01055926688"
        expect = "010-5592-6688"
        expect_g1 = "010"
        expect_g2 = "5592-6688"

        # when
        actual1 = comUtil.PhoneNumValidate(value=phoneNum_01)
        actual2 = comUtil.PhoneNumValidate(value=phoneNum_02)
        actual3 = comUtil.PhoneNumValidate(value=phoneNum_03)
        actual_g1 = comUtil.PhoneNumValidate(value=phoneNum_01, groupNo=1)
        actual_g2 = comUtil.PhoneNumValidate(value=phoneNum_02, groupNo=2)

        # then
        self.assertEqual(expect, actual1)
        self.assertEqual(expect, actual2)
        # self.assertEqual(expect, actual3)
        self.assertEqual(expect_g1, actual_g1)
        self.assertEqual(expect_g2, actual_g2)

    def test_pipe(self):
        """
        파이프로 여러그룹 대조하기
            : | 문자는 여러개의 표현식 중 하나라도 일치하는지 대조하고 싶을때 사용.
        """
        # given
        heroRegex = re.compile(r'ScottBang|Fanatic Bang')

        mo = heroRegex.search("My name is Scottbang and before used Fanatic Bang.")
        print(mo.group())


    def test_qeustionMark(self):
        """
        물음표 기호 테스트
            : ? 문자는 그 앞에 있는 그룹이 선택적으로 대조하는 패턴이라고 지정하는 역확을 한다.
        :return:
        """
        regex = re.compile(r'Bat(wo)?man')
        mo1 = regex.search('The Adventures of Batman.')
        print(mo1.group())

        mo2 = regex.search('The Adventure of Batwoman.')
        print(mo2.group())

    def test_asterisk(self):
        """
        별표 기호 테스트
            : 0개 또는 기 이상과 일치
        :return:
        """
        regex = re.compile(r'Bat(wo)*man')
        mo1 = regex.search('The Adventures of Batman.')
        print(mo1.group())

        mo2 = regex.search('The Adventure of Batwoman.')
        print(mo2.group())

        mo3 = regex.search('The Adventure of Batwowowowoman.')
        print(mo3.group())


    def test_plus(self):
        """
        더하기 기호 테스트
            : 1개 또는 기 이상과 일치
        :return:
        """
        regex = re.compile(r'Bat(wo)+man')
        mo1 = regex.search('The Adventures of Batman.')
        # print(mo1.group())      # error

        mo2 = regex.search('The Adventure of Batwoman.')
        print(mo2.group())


    def test_braces(self):
        """
        {} 중괄호 기호 테스트
            : 특정 횟수만큼 반복기호
        :return:
        """
        regex = re.compile(r'Bat(wo){2}man')
        mo1 = regex.search('The Adventures of Batwoman.')
        # print(mo1.group())      # error

        mo2 = regex.search('The Adventure of Batwowoman.')
        print(mo2.group())


    def test_minmax(self):
        """
        최대 일치와 최소 일치
            : 반복 횟수의 범위 지정 기호
        :return:
        """
        regex = re.compile(r'Bat(wo){2,5}man')
        # 2번
        mo1 = regex.search('The Adventures of Batwowoman.')
        print(mo1.group())
        # 5번
        mo2 = regex.search('The Adventure of Batwowowowowoman.')
        print(mo2.group())

        # 3번
        mo3 = regex.search('The Adventure of Batwowowoman.')
        print(mo3.group())

        # 6번
        mo3 = regex.search('The Adventure of Batwowowowowowoman.')
        # print(mo3.group())      # error







