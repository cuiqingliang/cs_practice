import pytest

from pytest_practice.core.calu import Calu


class Test_Calu:
    def setup_class(self):
        self.calu=Calu()

    @pytest.mark.parametrize('a,b,c',[
        [1, 0, 1],
        [2, -3, -1],
        [-2, 3, -1],
        [1.123456, 1.123456, 2.246912]
    ])
    def test_add(self,a,b,c):
        assert self.calu.add(a, b) == c
        print(self.calu.add(a, b), c)
    @pytest.mark.parametrize('a,b,c',[
        [1, 0, 1],
        [2, -3, 5],
        [-2, 3, -5],
        [1.123456, 1.123456,0 ]
    ])
    def test_jian(self,a,b,c):
        assert self.calu.jian(a, b) == c
        print(self.calu.jian(a, b), c)


    @pytest.mark.parametrize('a,b,c', [
        [1, 0, 0],
        [2, 1, 2],
        [-2, 3, -6],
        [1.123456, 1.123456, 1.262153383936]
    ])
    def test_mul(self,a,b,c):
        assert self.calu.mul(a,b) == c
        print(self.calu.mul(a,b),c)

    @pytest.mark.parametrize('a,b,c', [
        [2, 1, 2],
        [-2,3,-0.6666666666666667],
        [1.123456,1.123456,1]
    ])
    def test_div(self, a, b, c):
        assert self.calu.div(a,b) == c
        print(self.calu.div(a,b),c)

    @pytest.mark.parametrize('a,b,c', [
        [2, 1, 2],
        [-2, 3, -0.6666666666666667],
        [1.123456, 1.123456, 1]
    ])
    def test_process(self,a,b,c):
        d=self.calu.mul(a, b)
        print(d)
        print(self.calu.div(d, b), c)
        assert self.calu.div(d, b) == c

    @pytest.mark.parametrize('a,b,c', [
        [1, 'w', 2]
    ])
    def test_error1(self,a,b,c):

        with pytest.raises(TypeError):
            assert self.calu.add(a,b)==c
            assert self.calu.jian(a,b)==c
            assert self.calu.mul(a, b) == c
            assert self.calu.div(a, b) == c

    @pytest.mark.parametrize('a,b,c', [
        [1, 0, 2]
    ])
    def test_error2(self, a, b, c):
        with pytest.raises(ZeroDivisionError):
            assert self.calu.div(a, b) == c



