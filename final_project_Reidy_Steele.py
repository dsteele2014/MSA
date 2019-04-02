import unittest
import random
import time
import math


class msa_pricing:

    def msa_brute_force(self, pricelist):
        '''
            Implementation of the Brute Force maximum-subarray problem

            :param: pricelist: an array of prices
            :type pricelist: array
            :param: msa_max: running tally of maximum price
            :type msa_max: int
            :param: pricesum: sum of prices to compare to msa_max
            :type pricesum: int
            :return: a maximum subarray sum
            :rtype: int

        '''
        msa_max = 0
        for i in range(1, len(pricelist)):
            pricesum = 0
            for x in range(i, len(pricelist)):
                pricesum += (pricelist[x] - pricelist[x - 1])
                if pricesum > msa_max:
                    msa_max = pricesum
        return msa_max

    def msa_divide_and_conquer(self, updated_pricelist):
        '''
            Implementation of the Divide and Conquer MSA problem

            :param: pricelist: an array of prices
            :type pricelist: array
            :return: the sum of the maximum sub-array in the pricelist
            :rtype: int
        '''

        def find_msa(updated_pricelist, low, high):
            '''
                Recursive procedure returning the low, high, and sum of an array
                
                :param updated_pricelist: array being searched
                :param low: the index of the lowest point of the array
                :param high: the index of the highest point of the array
                :type update_pricelist: array
                :type low: int
                :type high: int
                :return: the lowest index of the current maximum sub-array, the highest index of the current maximum sub-array, the sum of the maximum sub-array
                :rtype: int, int, int
            '''

            if low == high:
                return (low, high, updated_pricelist[low])
            else:
                mid = math.floor((low + high) / 2)
                (left_low, left_high, left_sum) = find_msa(updated_pricelist, low, mid)
                (right_low, right_high, right_sum) = find_msa(updated_pricelist, mid + 1, high)
                (cross_low, cross_high, cross_sum) = find_crossing_msa(updated_pricelist, low, mid, high)
                if (left_sum >= right_sum) and (left_sum >= cross_sum):
                    return (right_low, right_high, right_sum)

                elif (right_sum >= left_sum) and (right_sum >= cross_sum):
                    return (right_low, right_high, right_sum)
                else:
                    return (cross_low, cross_high, cross_sum)

        def find_crossing_msa(updated_pricelist, low, mid, high):
            '''
                Returns the maximum sub-array of an array which the maximum crosses the mid point

                :param updated_pricelist: array being searched
                :param low: the index of the lowest point of the array
                :param mid: the index of the middle point of the array
                :param high: the index of the highest point of the array
                :type update_pricelist: array
                :type low: int
                :type mid: int
                :type high: int
                :return: the maximum position of the left sub-array, the maximum position of the right sub-array, the sum of the left sum and the right sum
                :rtype: int, int, int
            '''

            left_sum = -1000000000
            cross_sum = 0
            max_left = 0
            max_right = 0
            for i in range(mid, low, -1):
                cross_sum = cross_sum + updated_pricelist[i]
                if cross_sum > left_sum:
                    left_sum = cross_sum
                    max_left = i
            right_sum = -1000000000
            cross_sum = 0
            for j in range(mid + 1, high):
                cross_sum = cross_sum + updated_pricelist[j]
                if cross_sum > right_sum:
                    right_sum = cross_sum
                    max_right = j
            return (max_left, max_right, left_sum + right_sum)

        (low, high, max_sum) = find_msa(updated_pricelist, 0, len(updated_pricelist) - 1)
        return (max_sum)


class MSATest(unittest.TestCase):
    timer = []
    test_type = []
    test_size = []

    def setUp(self):
        self.msa = msa_pricing()

    ###########Tests for brute force###########

    def test_msa_bruteforce_fixed(self):
        pricelist = [100, 98, 102]
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertEqual(msa_max, 4)

    def test_msa_bruteforce_fixed2(self):
        pricelist = [100, 98, 102, 105, 75]
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertEqual(msa_max, 7)

    def test_msa_bruteforce_fixed3(self):
        pricelist = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertEqual(msa_max, 43)

    def test_msa_bruteforce_random_5(self):
        pricelist = [100]
        for x in range(5):
            pricelist.append(random.randint(50, 150))
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)

    def test_msa_bruteforce_random_1000(self):
        pricelist = [100]
        for x in range(1000):
            pricelist.append(random.randint(50, 150))
        start_time = time.time()
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Brute force random 1000")
        self.timer.append(time.time() - start_time)

    def test_msa_bruteforce_random_2000(self):
        pricelist = [100]
        for x in range(2000):
            pricelist.append(random.randint(50, 150))
        start_time = time.time()
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Brute force random 2000")
        self.timer.append(time.time() - start_time)

    def test_msa_bruteforce_random_3000(self):
        pricelist = [100]
        for x in range(3000):
            pricelist.append(random.randint(50, 150))
        start_time = time.time()
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Brute force random 3000")
        self.timer.append(time.time() - start_time)

    ###########Tests for divide and conquer###########

    def test_msa_divide_and_conquer_base(self):
        pricelist = [100]
        pricelist = MSATest.price_setup(pricelist)
        msa_max = self.msa.msa_divide_and_conquer(pricelist)
        self.assertEqual(msa_max, 0)

    def test_msa_divide_and_conquer_fixed2(self):
        pricelist = [100, 98, 102, 105, 75]
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertEqual(msa_max, 7)

    def test_msa_divide_and_conquer_fixed3(self):
        pricelist = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertEqual(msa_max, 43)

    def test_msa_divide_and_conquer_fixed(self):
        pricelist = [100, 98, 102]
        pricelist = MSATest.price_setup(pricelist)
        msa_max = self.msa.msa_divide_and_conquer(pricelist)
        self.assertEqual(msa_max, 4)

    def test_msa_divide_and_conquer_random_5(self):
        pricelist = [100]
        for x in range(5):
            pricelist.append(random.randint(50, 150))
        pricelist = MSATest.price_setup(pricelist)
        msa_max = self.msa.msa_divide_and_conquer(pricelist)
        self.assertIsNot(msa_max, 0)

    def test_msa_divide_and_conquer_random_1000(self):
        pricelist = [100]
        self.test_size.append(1000)
        for x in range(1000):
            pricelist.append(random.randint(50, 150))
        pricelist = MSATest.price_setup(pricelist)
        start_time = time.time()
        msa_max = self.msa.msa_divide_and_conquer(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Divide and Conquer random 1000")
        self.timer.append(time.time() - start_time)

    def test_msa_divide_and_conquer_random_2000(self):
        pricelist = [100]
        self.test_size.append(2000)
        for x in range(2000):
            pricelist.append(random.randint(50, 150))
        pricelist = MSATest.price_setup(pricelist)
        start_time = time.time()
        msa_max = self.msa.msa_divide_and_conquer(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Divide and Conquer random 2000")
        self.timer.append(time.time() - start_time)

    def test_msa_divide_and_conquer_random_3000(self):
        pricelist = [100]
        self.test_size.append(3000)
        for x in range(3000):
            pricelist.append(random.randint(50, 150))
        pricelist = MSATest.price_setup(pricelist)
        start_time = time.time()
        msa_max = self.msa.msa_divide_and_conquer(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Divide and Conquer random 3000")
        self.timer.append(time.time() - start_time)

    #############################

    def test_runtimes(self):
        print(self.test_size)
        for i in range(0, 3):
            print()
            print(self.test_type[i])
            expected = self.timer[0] * math.pow(i + 1, 2)
            print("Actual time" + "                    Expect time")
            print('{0}              {1}'.format(self.timer[i], expected))
            print("---------------------------------------------------")
        print("#####################################################")
        for i in range(3, len(self.timer)):
            print()
            expected = ((i-2)*self.timer[3])+(self.timer[3]*math.log(i-2))
            print("Actual time" + "                    Expect time")
            print('{0}              {1}'.format(self.timer[i], expected))
            print("---------------------------------------------------")

    def price_setup(pricelist):
        '''
            :param pricelist: the array to be updated
            :type: array
            :return: an updated array
            :rtype: array
        '''

        updated_pricelist = []
        for x in range(0, len(pricelist)):
            updated_pricelist.append(pricelist[x] - pricelist[x - 1])
        return updated_pricelist


def main():
    unittest.main()


if __name__ == '__main__':
    main()
