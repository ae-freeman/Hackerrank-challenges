package com.company;

public class Main {

    public static void main(String[] args) {
	staircase(6);
    }

    // Complete the staircase function below.
    public static void staircase(int n) {
        //check n is greater than 0 and less than 101
        if(n > 0 && n < 101){
            //if yes, print staircase
            int hashCounter = 1;
            int spaceCounter = n;
            for(int i = 0; i < n; i++){
                //print one line

                //print spaces
                for (int k = 1; k < spaceCounter; k++){
                    System.out.print(" ");
                }

                //print hashes
                for(int j = 0; j < hashCounter; j++){
                    System.out.print("#");
                }

                spaceCounter--;
                hashCounter++;
                //if i is less than n -2, start new line
                if (i < (n - 1)) {
                    System.out.println("");

                }

//

            }

        } else {
            System.out.println("Invalid number");
        }


    }
}
