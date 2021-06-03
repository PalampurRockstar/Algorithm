package com.algo;

public class CoinCombinationOnChange {

    public int coinCombinationWithMatrix(int total, int coins[]) {
        int temp[][] = new int[coins.length + 1][total + 1];
        temp[0][0] = 1;
        for (int i = 1; i <= coins.length; i++)
            for (int j = 0; j <= total; j++) {
                int currentCoin = coins[i - 1];
                if (currentCoin > j)
                    temp[i][j] = temp[i - 1][j];
                else
                    temp[i][j] = temp[i][j - currentCoin] + temp[i - 1][j];
            }
        return temp[coins.length][total];
    }

    public int coinCombinationWithArray(int total, int arr[]) {

        int temp[] = new int[total + 1];
        temp[0] = 1;
        for (int i = 0; i < arr.length; i++)
            for (int j = 1; j <= total; j++)
                if (j >= arr[i])
                    temp[j] += temp[j - arr[i]];
        return temp[total];
    }


    public static void main(String args[]) {
        CoinCombinationOnChange cc = new CoinCombinationOnChange();
        int total = 15;
        int coins[] = {3, 4, 6, 7, 9};
        System.out.println(cc.coinCombinationWithMatrix(total, coins));
        System.out.println(cc.coinCombinationWithArray(total, coins));

    }
}
