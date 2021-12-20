import sum

# у меня не проходят тесты. В функции из основного файла все переменнные как none

class TestSumm: 
    def test_sum_1_4_7(self):
        assert sum.summ(1, 4, 7) == 12

    def test_sum_22_3_5_10(self):
        assert sum.summ(22, 3, 5, 10) == 40