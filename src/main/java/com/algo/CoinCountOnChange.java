package com.algo;

public class CoinCountOnChange {


    public int countWithMatrix(int total, int coins[]) {
        int temp[][] = new int[coins.length + 1][total];
        for (int i = 0; i <= coins.length; i++)
            for (int j = 0; j < total; j++) {
                if (i == 0) {
                    temp[i][j] = Integer.MAX_VALUE - 1;
                } else if (j + 1 == coins[i - 1]) {
                    temp[i][j] = 1;
                } else {
                    int currentCoin = coins[i - 1];
                    if (currentCoin > j)
                        temp[i][j] = temp[i - 1][j];
                    else
                        temp[i][j] = Math.min(temp[i][j - currentCoin] + 1, temp[i - 1][j]);
                }
            }
        return temp[coins.length][total - 1];
    }

    public int countWithSingleArray(int total, int coins[]) {
        int CC[] = new int[total + 1];
        CC[0] = 0;
        for (int j = 0; j < coins.length; j++)
            for (int i = 1; i <= total; i++) {
                if (j == 0)
                    CC[i] = Integer.MAX_VALUE - 1;
                if (i >= coins[j] && CC[i - coins[j]] + 1 < CC[i])
                    CC[i] = 1 + CC[i - coins[j]];
            }
        return CC[total];
    }


    public static void main(String args[]) {
        CoinCountOnChange cc = new CoinCountOnChange();
        int total = 15;
        int coins[] = {3, 4, 6, 7, 9};
        System.out.println(cc.countWithSingleArray(total, coins));
        System.out.println(cc.countWithMatrix(total, coins));
    }
}
