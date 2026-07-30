import java.util.Arrays;

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;
        
        while (h < n && citations[n - 1 - h] > h) {
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