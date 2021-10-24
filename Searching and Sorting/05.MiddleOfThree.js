// Problem link - https://practice.geeksforgeeks.org/problems/middle-of-three2926/1

class Solution {
    middle(A, B, C) {
        if (A > B) {
            if (B > C) {
                return B
            }
            if (A < C) {
                return A
            }
            return C
        } else {
            if (A > C) {
                return A
            }
            if (B > C) {
                return C
            }
            return B
        }
    }
}