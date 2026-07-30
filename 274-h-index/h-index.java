
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;

        Arrays.sort(citations); // Sorts in ascending order: [1, 3, 5]
// Reverse the array in-place
        for (int i = 0; i < citations.length / 2; i++) {
            int temp = citations[i];
            citations[i] = citations[citations.length - 1 - i];
            citations[citations.length - 1 - i] = temp;
        }

        
        while (h < n && citations[h] > h) {
            h++;
        }
        
        return h;
    }
}

// class Solution {
//     public int hIndex(int[] citations) {
//         Arrays.sort(citations);
//         int n = citations.length;
        
//         for (int i = 0; i < n; i++) {
//             if (citations[i] >= n - i) {
//                 return n - i;
//             }
//         }
        
//         return 0;
//     }
// }