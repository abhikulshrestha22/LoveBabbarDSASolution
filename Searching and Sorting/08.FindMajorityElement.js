class Solution {

    majorityElement(a, size) {
        let max_count = 1
        let max_val = a[0]
        let count = 1
        a.sort((a, b) => a - b)
        for (let i = 1; i < size; i++) {
            if (a[i - 1] === a[i]) {
                count += 1
                if (count > max_count) {
                    max_count = count;
                    max_val = a[i]
                }
            } else {
                count = 1
            }
        }
        if (max_count > size / 2) {
            return max_val
        }
        return -1

    }
}